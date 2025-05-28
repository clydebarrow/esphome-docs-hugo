
const bodystyle = window.getComputedStyle(document.body);
const mobileWidthStop = parseInt(bodystyle.getPropertyValue('--mobile-width-stop'));
const isMobile = (window.innerWidth <= mobileWidthStop);

function openTOC() {
    const tocToggle = document.getElementById('toc-toggle');
    if (!isMobile || !tocToggle) return;
    const tocPanel = document.getElementsByClassName('sidebar')[0];
    const overlay = document.getElementById('overlay');
    tocToggle.classList.add('open');
    tocPanel.classList.add('open');
    overlay.classList.add('show');
}

function closeTOC() {
    const tocToggle = document.getElementById('toc-toggle');
    if (!isMobile || !tocToggle) return;
    const tocPanel = document.getElementsByClassName('sidebar')[0];
    const overlay = document.getElementById('overlay');
    tocToggle.classList.remove('open');
    tocPanel.classList.remove('open');
    overlay.classList.remove('show');
}

// Add keyboard support for dropdown menus
document.addEventListener('DOMContentLoaded', function() {

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        document.querySelector('.theme-toggle').setAttribute('aria-label', `Toggle ${theme === 'dark' ? 'light' : 'dark'} mode`);
        closeMenu();
    }

    // Theme toggle functionality
    const themeToggle = document.querySelector('.theme-toggle');
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        setTheme(currentTheme === 'dark' ? 'light' : 'dark');
    });

    const tocToggle = document.getElementById('toc-toggle');
    const overlay = document.getElementById('overlay');
    if (tocToggle)
        tocToggle.addEventListener('click', openTOC);
    if (overlay)
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

    function closeMenu() {
        navLinks.classList.remove('active');
        hamburger.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
    }
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
            closeMenu();
        }
    });
    // Close menu on resize to desktop
    window.addEventListener('resize', function() {
        if (window.innerWidth > mobileWidthStop) {
            closeMenu();
        }
    });

    // Search functionality
    if (typeof PagefindModularUI === 'undefined') {
        console.error('PagefindModularUI library not loaded');
        return;
    }


    class El {
        constructor(tagname) {
            this.element = document.createElement(tagname);
        }

        id(s) {
            this.element.id = s;
            return this;
        }

        class(s) {
            this.element.classList.add(s);
            return this;
        }

        attrs(obj) {
            for (const [k, v] of Object.entries(obj)) {
                this.element.setAttribute(k, v);
            }
            return this;
        }

        text(t) {
            this.element.innerText = t;
            return this;
        }

        html(t) {
            this.element.innerHTML = t;
            return this;
        }

        handle(e, f) {
            this.element.addEventListener(e, f);
            return this;
        }

        addTo(el) {
            if (el instanceof El) {
                el.element.appendChild(this.element);
            } else {
                el.appendChild(this.element);
            }
            return this.element;
        }
    }

    function getLink(location, anchors, url) {
        if (!anchors || !anchors.length)
            return null;
        // find the closest anchor at or before the current location
        const anchor = anchors.sort((a, b) => b.location - a.location).find(a => a.location <= location);
        if (anchor) {
            return url + "#" + anchor.id;
        }
        return null;
    }

    const resultTemplate = (result) => {
        const wrapper = new El("li").class("pagefind-modular-list-result");
        wrapper.handle("click", closeResults);

        const thumb = new El("div").class("pagefind-modular-list-thumb").addTo(wrapper);
        let image = result?.meta?.image;
        if (image) {
            if (image.includes("/_images/"))
                image = image.substring(image.indexOf("/_images/"));
            new El("img").class("pagefind-modular-list-image").attrs({
                src: image,
                alt: result.meta.image_alt || result.meta.title
            }).addTo(thumb);
        }

        const inner = new El("div").class("pagefind-modular-list-inner").addTo(wrapper);
        const title = new El("p").class("pagefind-modular-list-title").addTo(inner);
        new El("a").class("pagefind-modular-list-link").text(result.meta?.title).attrs({
            href: result.meta?.url || result.url
        }).addTo(title);

        const excerpt = new El("p").class("pagefind-modular-list-excerpt").addTo(inner);
        const locations = result.weighted_locations.sort((a, b) => b.weight - a.weight);
        const url = getLink(locations[0]?.location, result.anchors, result.url) || result.meta?.url || result.url;
        new El("a").class("pagefind-modular-list-link").html(result.excerpt).attrs({
            href: url
        }).addTo(excerpt);

        return wrapper.element;
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

    const resultsContainer = document.getElementById('nav-search-results');

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
        containerElement: "#nav-search-results",
        resultTemplate: resultTemplate
    }));


    let top_hit = null;

    function closeResults() {
        resultsContainer.style.display = 'none';
        top_hit = null;
    }

    // Show/hide results
    instance.on("results", async (results) => {
        if (results.results.length) {
            resultsContainer.style.display = 'block';
            const data = await results.results[0].data();
            top_hit = data.url;
            console.log(data);
        } else {
            closeResults();
        }
    });

    document.addEventListener('click', function(e) {
        if (!e.target.closest('#nav-search-results')) {
            closeResults();
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


});
