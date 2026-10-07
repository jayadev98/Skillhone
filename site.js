(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
      }
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
        toggle.focus();
      }
    });
  }

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  const form = document.querySelector('#requirement-form');
  if (form) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;

      const values = new FormData(form);
      const fields = [
        ['Organisation Name', 'organisation'], ['Industry / Sector', 'industry'],
        ['Contact Person', 'contactPerson'], ['Designation / Role', 'designation'],
        ['Email', 'email'], ['Contact Number', 'phone'],
        ['Training Requirement / Topic', 'topic'], ['Business Context / Background', 'businessContext'],
        ['Current Challenges / Performance Gaps', 'challenges'], ['Target Audience', 'audience'],
        ['Participant Profile', 'participantProfile'], ['Expected Learning Outcomes', 'learningOutcomes'],
        ['Business Outcomes Expected', 'businessOutcomes'], ['Preferred Training Format', 'format'],
        ['Preferred Duration', 'duration'], ['Expected Number of Participants', 'participants'],
        ['Proposed Timeline', 'timeline'], ['Location', 'location'],
        ['Existing Interventions', 'interventions'], ['Assessment / Evaluation Requirements', 'assessment'],
        ['Additional Information / Specific Expectations', 'additionalInfo']
      ];
      const body = fields.map(([label, name]) => `${label}: ${values.get(name) || '—'}`).join('\n\n');
      const subject = `Training requirement enquiry — ${values.get('organisation')}`;
      const mailto = `mailto:mahesh@skillhone.in?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      const status = document.querySelector('#form-status');
      if (status) status.textContent = 'Your email app should open with the request prepared. Review the details and send the email to complete your enquiry.';
      window.location.href = mailto;
    });
  }
})();
