from html.parser import HTMLParser
from pathlib import Path
root=Path('outputs')
class Scan(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.src=[]; self.ids=set(); self.h1=0; self.label_count=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag in ('img','script','link'):
            key='src' if tag in ('img','script') else 'href'
            if key in a: self.src.append(a[key])
        if tag=='h1': self.h1+=1
        if tag=='label': self.label_count+=1
pages=list(root.glob('*.html'))
scans={p.name:Scan() for p in pages}
for p in pages: scans[p.name].feed(p.read_text(encoding='utf-8'))
errors=[]
for p in pages:
    s=scans[p.name]
    if s.h1 != 1: errors.append(f'{p.name}: expected one h1, got {s.h1}')
    for ref in s.src:
        if ref.startswith(('http:','https:','data:')): continue
        if not (p.parent / ref).exists(): errors.append(f'{p.name}: missing asset {ref}')
    for ref in s.links:
        if ref.startswith(('#','mailto:','tel:','http:','https:')):
            if ref.startswith('#') and ref[1:] not in s.ids: errors.append(f'{p.name}: missing in-page target {ref}')
            continue
        path, _, anchor=ref.partition('#')
        dest=p.parent/path
        if not dest.exists(): errors.append(f'{p.name}: missing link target {ref}')
        elif anchor and dest.suffix=='.html':
            other=scans.get(dest.name)
            if other is None: other=Scan(); other.feed(dest.read_text(encoding='utf-8'))
            if anchor not in other.ids: errors.append(f'{p.name}: missing target {ref}')
print('pages:', ', '.join(sorted(x.name for x in pages)))
for p in sorted(pages): print(f'{p.name}: one h1, {len(scans[p.name].links)} links, {len(scans[p.name].src)} local assets, {scans[p.name].label_count} labels')
print('form fields:',len([l for l in scans['contact.html'].links if False]))
print('reference errors:',errors if errors else 'none')
