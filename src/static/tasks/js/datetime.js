document.addEventListener("DOMContentLoaded", function () {
    const dateTimeInput = document.querySelector('input[type="datetime-local"]');
    
    if (dateTimeInput) {
        if (!dateTimeInput.value) {
            const now = new Date();
            const formattedValue = now.toISOString().slice(0, 16);
            dateTimeInput.value = formattedValue;
        }

        dateTimeInput.addEventListener('change', function (event) {
            const inputValue = event.target.value;
            console.log('Formatted date for Django:', inputValue);
        });
    }
});

