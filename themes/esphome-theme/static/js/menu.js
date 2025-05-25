
const bodystyle = window.getComputedStyle(document.body);
const mobileWidthStop = parseInt(bodystyle.getPropertyValue('--mobile-width-stop'));
const isMobile = (window.innerWidth <= mobileWidthStop);

function openTOC() {
    if (!isMobile) return;
    const tocPanel = document.getElementsByClassName('sidebar')[0];
    const overlay = document.getElementById('overlay');
    const tocToggle = document.getElementById('toc-toggle');
    tocToggle.classList.add('open');
    tocPanel.classList.add('open');
    overlay.classList.add('show');
}

function closeTOC() {
    const tocPanel = document.getElementsByClassName('sidebar')[0];
    const overlay = document.getElementById('overlay');
    const tocToggle = document.getElementById('toc-toggle');
    tocToggle.classList.remove('open');
    tocPanel.classList.remove('open');
    overlay.classList.remove('show');
}

// Add keyboard support for dropdown menus
document.addEventListener('DOMContentLoaded', function() {

    const tocToggle = document.getElementById('toc-toggle');
    const overlay = document.getElementById('overlay');

    tocToggle.addEventListener('click', openTOC);
    overlay.addEventListener('click', closeTOC);

    const dropdownButtons = document.querySelectorAll('.dropbtn button');

    dropdownButtons.forEach(button => {
        // Handle Enter and Space key presses
        button.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleDropdown(this);
            }
        });

        // Handle click events
        button.addEventListener('click', function(e) {
            if (!isMobile) return;
            e.preventDefault();
            // Close others
            dropdownButtons.forEach(function(otherBtn) {
                if (otherBtn !== button) {
                    otherBtn.setAttribute('aria-expanded', 'false');
                    if (otherBtn.nextElementSibling) {
                        otherBtn.nextElementSibling.style.display = 'none';
                    }
                }
            });
            // Toggle this one
            const expanded = button.getAttribute('aria-expanded') === 'true';
            button.setAttribute('aria-expanded', expanded ? "false" : "true");
            if (button.nextElementSibling) {
                button.nextElementSibling.style.display = expanded ? 'none' : 'block';
            }
        });
    });

    // Close dropdowns when Escape key is pressed
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape') {
            closeAllDropdowns();
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.matches('.dropbtn')) {
            closeAllDropdowns();
        }
    });

    // Toggle dropdown function
    function toggleDropdown(button) {
        if (window.innerWidth > mobileWidthStop) return;
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
        closeAllDropdowns();

        if (!isExpanded) {
            button.setAttribute('aria-expanded', 'true');
            const dropdownContent = button.nextElementSibling;
            dropdownContent.style.display = 'block';
        }
    }

    // Close all dropdowns
    function closeAllDropdowns() {
        if (window.innerWidth > mobileWidthStop) return;
        dropdownButtons.forEach(btn => {
            btn.setAttribute('aria-expanded', 'false');
            const dropdownContent = btn.nextElementSibling;
            if (dropdownContent)
                dropdownContent.style.display = 'none';
        });
    }


    const hamburger = document.querySelector('.hamburger-button');
    const navLinks = document.querySelector('.nav-links');
    if (!hamburger || !navLinks) return;
    hamburger.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        const expanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', expanded ? "false" : "true");
        closeTOC();
    });
    // Close menu on outside click (mobile only)
    document.addEventListener('click', function(e) {
        if (window.innerWidth > mobileWidthStop) return;
        if (!e.target.closest('.hamburger-button') && !e.target.closest('.nav-links')) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });
    // Close menu on resize to desktop
    window.addEventListener('resize', function() {
        if (window.innerWidth > mobileWidthStop) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });


    // Search functionality
    if (typeof PagefindModularUI === 'undefined') {
        console.error('PagefindModularUI library not loaded');
        return;
    }

    // Create search input and container
    const searchContainer = document.getElementById('nav-search-container');

    // Create search input
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.id = "frontpage-search";
    searchInput.placeholder = 'Search...';
    searchInput.className = 'pagefind-ui__search-input';
    searchContainer.appendChild(searchInput);

    // Create search results container
    const resultsContainer = document.getElementById('nav-search-results');

    // Initialize PagefindModularUI
    const instance = new PagefindModularUI.Instance({
        showSubResults: true,
        showImages: false,
        resetStyles: true,
        ranking: {
            pageLength: 0.0,
            termSaturation: 1.6,
            termFrequency: 0.4,
            termSimilarity: 6.0
        }
    });

    // Add input component
    instance.add(new PagefindModularUI.Input({
        inputElement: "#frontpage-search"
    }));

    // Add results component
    instance.add(new PagefindModularUI.ResultList({
        containerElement: "#nav-search-results"
    }));

    let top_hit = null;

    // Show/hide results
    instance.on("results", async (results) => {
        if (results.results.length) {
            resultsContainer.style.display = 'block';
            data = await results.results[0].data();
            top_hit = data.url;
        } else {
            resultsContainer.style.display = 'none';
            top_hit = null;
        }
    });

    // Create clear button
    const clearButton = document.createElement('button');
    clearButton.type = 'button';
    clearButton.className = 'search-clear-button';
    clearButton.innerHTML = '<i class="fas fa-times"></i>';
    clearButton.style.display = 'none';
    searchContainer.appendChild(clearButton);

    // Show/hide clear button based on input content
    searchInput.addEventListener('input', () => {
        clearButton.style.display = searchInput.value.length > 0 ? 'flex' : 'none';
    });

    // Clear search when button is clicked
    clearButton.addEventListener('click', () => {
        searchInput.value = '';
        clearButton.style.display = 'none';
        instance.triggerSearch('');
        resultsContainer.style.display = 'none';
        searchInput.focus(); // Re-focus the search box after clearing
    });

    document.addEventListener('keydown', function(event) {
        if (!(searchInput === document.activeElement) && event.key === '/') { // Use '/' key as trigger
            searchInput.focus();
            event.preventDefault(); // Prevent the '/' key from being entered in the search box
        }
    });

    const navContainer = document.getElementById('nav-container');

    searchInput.addEventListener('focusin', () => {
        navContainer.style.transform = `translateY(0)`;
    });
    searchInput.addEventListener('beforeinput', () => {
        navContainer.style.transform = `translateY(0)`;
    });
    searchInput.addEventListener('keydown', function(event) {
        if (event.key === "Enter" && !!top_hit) {
            window.location = top_hit;
            top_hit = null;
        }
    });


    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        document.querySelector('.theme-toggle').setAttribute('aria-label', `Toggle ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }

    // Theme toggle functionality
    const themeToggle = document.querySelector('.theme-toggle');
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        setTheme(currentTheme === 'dark' ? 'light' : 'dark');
    });

});
