const htmlElement = document.getElementById('html-theme');
const themeToggleBtn = document.getElementById('theme-toggle');
const addTaskButton = document.getElementById('add-task-button');
    
function setTheme(theme) {
    htmlElement.setAttribute('data-bs-theme', theme);
    localStorage.setItem('theme', theme);

    if (theme === 'dark') {
        addTaskButton.classList.remove('btn-dark');
        addTaskButton.classList.add('btn-secondary');
    } else {
        addTaskButton.classList.remove('btn-secondary');
        addTaskButton.classList.add('btn-dark');
    }
}

const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

themeToggleBtn.addEventListener('click', () => {
    const currentTheme = htmlElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
});

