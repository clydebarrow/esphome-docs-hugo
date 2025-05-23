

function trapScroll(el) {
  el.addEventListener('wheel', (e) => {
    const scrollTop = el.scrollTop;
    const scrollHeight = el.scrollHeight;
    const offsetHeight = el.offsetHeight;
    const delta = e.deltaY;

    const atTop = scrollTop === 0;
    const atBottom = scrollTop + offsetHeight >= scrollHeight;

    if ((atTop && delta < 0) || (atBottom && delta > 0)) {
      e.preventDefault();
    }
  }, { passive: false });
}

function trapTouchScroll(el) {
  let startY = 0;

  el.addEventListener('touchstart', (e) => {
    startY = e.touches[0].clientY;
  });

  el.addEventListener('touchmove', (e) => {
    const scrollTop = el.scrollTop;
    const scrollHeight = el.scrollHeight;
    const offsetHeight = el.offsetHeight;
    const currentY = e.touches[0].clientY;
    const deltaY = currentY - startY;

    const atTop = scrollTop === 0;
    const atBottom = scrollTop + offsetHeight >= scrollHeight;

    if ((atTop && deltaY > 0) || (atBottom && deltaY < 0)) {
      e.preventDefault();
    }
  }, { passive: false });
}

document.addEventListener('DOMContentLoaded', function() {

  const scrollers = document.querySelectorAll('.scroll-trap');

  for (let i = 0; i !== scrollers.length; i++) {
    trapScroll(scrollers[i]);
    trapTouchScroll(scrollers[i]);
  }

  const scrollThreshold = 5; // Minimum scroll amount before triggering hide/show
  const navContainer = document.getElementById('nav-container');
  let scrollDelta = 0; // Track cumulative scroll amount
  let lastScrollTop = 0;


  function scroll_bar(newDelta) {
    let navHeight = navContainer.offsetHeight;
    // Remove the transition class when scrolling down for direct tracking
    navContainer.classList.remove('nav-scrolling-up');

    // Increase the scroll delta by the amount scrolled - start immediately from top
    scrollDelta += newDelta;

    // Cap the scroll delta at the nav height
    console.log("Original scrolldelta", scrollDelta, "navHeight", navHeight);
    scrollDelta = Math.min(scrollDelta, navHeight);
    console.log("New scrolldelta", scrollDelta);

    // Apply the transform
    navContainer.style.transform = `translateY(-${scrollDelta}px)`;

    // If fully hidden, add the nav-hidden class
    if (scrollDelta >= navHeight) {
      navContainer.classList.add('nav-hidden');
    }
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('a'); // Find nearest <a>
    if (link) {
      window.setTimeout( () => {
        scroll_bar(navContainer.offsetHeight);
      }, 200);
    }
  });

  // Header scroll behavior
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
      scroll_bar(currentScrollTop - lastScrollTop);
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

