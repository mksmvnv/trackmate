const htmlElement = document.getElementById('html-theme');
const themeToggleBtn = document.getElementById('theme-toggle');
const addTaskButton = document.getElementById('add-task-button');


function setTheme(themeName) {
    htmlElement.setAttribute('data-bs-theme', themeName);
    localStorage.setItem('theme', themeName);

    const isTasksPage = window.location.pathname === '/tasks/';
    const taskButton = document.getElementById('add-task-button');

    if (themeName === 'dark') {
        if (isTasksPage) {
            taskButton.classList.replace('btn-dark', 'btn-secondary');
        }
    } else {
        if (isTasksPage) {
            taskButton.classList.replace('btn-secondary', 'btn-dark');
        }
    }
}

const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

themeToggleBtn.addEventListener('click', () => {
    const currentTheme = htmlElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
});

