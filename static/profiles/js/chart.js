document.addEventListener('DOMContentLoaded', function() {
    const userId = document.getElementById('user-id').getAttribute('data-user-id');

    async function fetchTaskStatus() {
        try {
            const response = await fetch(`/api/task-status/${userId}/`);
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching task status', error);
            return { in_progress: 0, completed: 0 };
        }
    }

    async function createChart() {
        const data = await fetchTaskStatus();
        const ctx = document.getElementById('taskStatusChart').getContext('2d');

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['В процессе', 'Завершено'],
                datasets: [{
                    label: 'Статус задач',
                    data: [data.in_progress || 0, data.completed || 0],
                    backgroundColor: ['#9B82F7', '#FBE7A2'],
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 30,
                        }
                    },
                    maintainAspectRatio: false,
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return tooltipItem.label + ': ' + tooltipItem.raw;
                            }
                        }
                    }
                }
            }
        });
    }

    createChart();
});