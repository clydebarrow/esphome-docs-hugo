document.addEventListener('DOMContentLoaded', function() {
  // Mobile navigation toggle
  const hamburgerButton = document.querySelector('.hamburger-button');
  const navLinks = document.querySelector('.nav-links');
  
  if (hamburgerButton && navLinks) {
    hamburgerButton.addEventListener('click', function() {
      const expanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !expanded);
      navLinks.classList.toggle('active');
    });
  }
  
  // Dropdown menus for mobile
  const dropbtns = document.querySelectorAll('.dropbtn');
  
  dropbtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
      if (window.innerWidth <= 875) {
        e.preventDefault();
        const expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !expanded);
        
        const dropdown = this.nextElementSibling;
        if (dropdown) {
          dropdown.style.display = expanded ? 'none' : 'block';
        }
      }
    });
  });
  
  // Close dropdowns when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.matches('.dropbtn')) {
      dropbtns.forEach(btn => {
        const dropdown = btn.nextElementSibling;
        if (dropdown && dropdown.style.display === 'block' && window.innerWidth <= 875) {
          dropdown.style.display = 'none';
          btn.setAttribute('aria-expanded', 'false');
        }
      });
    }
  });
  
  // Simple search functionality
  const searchInput = document.getElementById('sidebar-search-input');
  
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const query = this.value.toLowerCase();
      const links = document.querySelectorAll('.sidebar-nav a');
      
      links.forEach(link => {
        const text = link.textContent.toLowerCase();
        if (text.includes(query)) {
          link.style.display = 'block';
        } else {
          link.style.display = 'none';
        }
      });
    });
  }
});
