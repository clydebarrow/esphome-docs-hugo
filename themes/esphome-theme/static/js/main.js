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
  
  // Header scroll behavior
  const navContainer = document.getElementById('nav-container');
  let lastScrollTop = 0;
  let scrollThreshold = 5; // Minimum scroll amount before triggering hide/show
  let navHeight = navContainer.offsetHeight;
  let scrollDelta = 0; // Track cumulative scroll amount
  let ticking = false; // Flag to prevent multiple rAF calls
  
  function handleScroll() {
    const currentScrollTop = window.scrollY || document.documentElement.scrollTop;
    
    // Check if we've scrolled more than the threshold
    if (Math.abs(lastScrollTop - currentScrollTop) <= scrollThreshold) {
      ticking = false;
      return;
    }
    
    // Scrolling down - directly track the scroll position
    if (currentScrollTop > lastScrollTop) {
      // Remove the transition class when scrolling down for direct tracking
      navContainer.classList.remove('nav-scrolling-up');
      
      // Increase the scroll delta by the amount scrolled - start immediately from top
      scrollDelta += (currentScrollTop - lastScrollTop);
      
      // Cap the scroll delta at the nav height
      scrollDelta = Math.min(scrollDelta, navHeight);
      
      // Apply the transform
      navContainer.style.transform = `translateY(-${scrollDelta}px)`;
      
      // If fully hidden, add the nav-hidden class
      if (scrollDelta >= navHeight) {
        navContainer.classList.add('nav-hidden');
      }
    } 
    // Scrolling up - smooth transition back
    else if (currentScrollTop < lastScrollTop) {
      // Reset the scroll delta
      scrollDelta = 0;
      
      // Add transition class for smooth appearance
      navContainer.classList.add('nav-scrolling-up');
      navContainer.classList.remove('nav-hidden');
      navContainer.style.transform = 'translateY(0)';
    }
    
    lastScrollTop = currentScrollTop;
    ticking = false;
  }
  
  // Use requestAnimationFrame for better performance
  window.addEventListener('scroll', function() {
    if (!ticking) {
      requestAnimationFrame(handleScroll);
      ticking = true;
    }
  });
  
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
