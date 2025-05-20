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
  
  // Table of Contents highlighting
  const tocLinks = document.querySelectorAll('.page-toc a');
  if (tocLinks.length > 0) {
    // Get all headings that correspond to TOC entries
    const headings = Array.from(tocLinks).map(link => {
      const id = link.getAttribute('href').substring(1);
      return document.getElementById(id);
    }).filter(Boolean);

    // Function to determine which heading is currently in view
    function findActiveHeading() {
      // Get current scroll position with a small offset to highlight section a bit earlier
      const scrollPosition = window.scrollY + 100;
      
      // Find the last heading that is above the current scroll position
      for (let i = headings.length - 1; i >= 0; i--) {
        if (headings[i].offsetTop <= scrollPosition) {
          return headings[i];
        }
      }
      
      // If no heading is found, return the first one
      return headings[0];
    }

    // Function to update active TOC item
    function updateActiveTocItem() {
      // Remove active class from all TOC links
      tocLinks.forEach(link => link.classList.remove('active'));
      
      // Find the active heading
      const activeHeading = findActiveHeading();
      if (activeHeading) {
        // Find the corresponding TOC link and add active class
        const activeLink = document.querySelector(`.page-toc a[href="#${activeHeading.id}"]`);
        if (activeLink) {
          activeLink.classList.add('active');
        }
      }
    }

    // Update on scroll (with debounce for performance)
    let scrollTimeout;
    window.addEventListener('scroll', function() {
      if (scrollTimeout) {
        clearTimeout(scrollTimeout);
      }
      scrollTimeout = setTimeout(updateActiveTocItem, 100);
    });

    // Initial update
    updateActiveTocItem();

    // Add smooth scrolling to TOC links
    tocLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80, // Offset for fixed header
            behavior: 'smooth'
          });
          
          // Update URL hash without jumping
          history.pushState(null, null, `#${targetId}`);
          
          // Update active TOC item
          updateActiveTocItem();
        }
      });
    });
  }
});
