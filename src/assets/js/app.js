document.addEventListener('DOMContentLoaded', () => {
  const root = document.documentElement;

  // Initialize theme from localStorage if available
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    root.setAttribute('data-theme', savedTheme);
  } else {
    // If no saved theme, wait for the first render to set it according to system if needed
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (systemPrefersDark) {
      root.setAttribute('data-theme', 'dark');
    }
  }

  // Handle HTML Invoker commands (native behavior in modern browsers supporting 'command' event)
  root.addEventListener('command', (event) => {
    if (event.command === '--toggle-theme') {
      const currentTheme = root.getAttribute('data-theme') || 
                           (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      
      root.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // If we're using view transitions, doing it here might be tricky natively without JS wrapper,
      // but view transition for navigation is already handled by CSS.
    }
  });

  // Headerbar scroll effect
  const headerbar = document.querySelector('.headerbar');
  const windowContent = document.querySelector('.window-content');
  
  if (headerbar && windowContent) {
    windowContent.addEventListener('scroll', () => {
      if (windowContent.scrollTop > 0) {
        headerbar.classList.add('scrolled');
      } else {
        headerbar.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // Dialog Headerbar scroll effect
  const dialogContents = document.querySelectorAll('.dialog-content');
  dialogContents.forEach(content => {
    content.addEventListener('scroll', () => {
      const header = content.previousElementSibling;
      if (header && header.classList.contains('headerbar')) {
        if (content.scrollTop > 0) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      }
    }, { passive: true });
  });

  // Small polyfill/helper in case 'commandfor' on dialog isn't fully supported without polyfill yet
  // This ensures our dialogs close/open properly if the browser doesn't fully support Invoker Commands.
  if (!window.HTMLButtonElement.prototype.hasOwnProperty('commandForElement')) {
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('[commandfor]');
      if (!btn) return;

      const targetId = btn.getAttribute('commandfor');
      const targetElement = document.getElementById(targetId);
      const command = btn.getAttribute('command');
      
      if (!targetElement) {
        if (targetId === 'html-root' && command === '--toggle-theme') {
            root.dispatchEvent(new Event('command'));
            // Since we dispatch a mock event above, let's manually mock the event property:
            const customEvent = new Event('command');
            customEvent.command = '--toggle-theme';
            root.dispatchEvent(customEvent);
        }
        return;
      }

      if (targetElement.tagName === 'DIALOG') {
        if (command === 'show-modal') {
          targetElement.showModal();
        } else if (command === 'close') {
          targetElement.close();
        }
      }
    });
  }
});
