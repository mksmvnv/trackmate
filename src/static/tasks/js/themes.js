// Dark mode

const htmlElement = document.getElementById('html-theme');
const themeIcon = document.getElementById('theme-icon');
const themeToggleBtn = document.getElementById('theme-toggle');
const themePaginations = document.querySelectorAll('.theme-pagination');


function setTheme(themeName) {
    htmlElement.setAttribute('data-bs-theme', themeName);
    localStorage.setItem('theme', themeName);

    // Change icon

    if (themeName === 'dark') {
        themeIcon.classList.replace('bi-brightness-high', 'bi-moon');
    } else {
        themeIcon.classList.replace('bi-moon', 'bi-brightness-high');
    }

    // Change pagination color

    themePaginations.forEach(themePagination => {
        if (themeName === 'dark') {
            themePagination.style.color = '#fff';
        } else {
            themePagination.style.color = '#000';
        }
    });
}

const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

themeToggleBtn.addEventListener('click', () => {
    const currentTheme = htmlElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
});
