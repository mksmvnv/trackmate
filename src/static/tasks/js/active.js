// Active navbar

const navbarTasks = document.getElementById('navbar-tasks');
const navbarActivity = document.getElementById('navbar-activity');
const navbarProfile = document.getElementById('navbar-profile');

function setActiveNavbar() {
    const path = window.location.pathname;
    if (path.includes('/tasks/')) {
        navbarTasks.classList.add('active');
        navbarActivity.classList.remove('active');
        navbarProfile.classList.remove('active');
    } else if (path.includes('/activity/')) {
        navbarActivity.classList.add('active');
        navbarTasks.classList.remove('active');
        navbarProfile.classList.remove('active');
    } else if (path.includes('/profiles/')) {
        navbarProfile.classList.add('active');
        navbarTasks.classList.remove('active');
        navbarActivity.classList.remove('active');
    }
}

setActiveNavbar();