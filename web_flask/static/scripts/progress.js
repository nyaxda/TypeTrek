document.addEventListener('DOMContentLoaded', function() {
        const labels = progressData.map(record => record.exercise_title);
        const accuracyData = progressData.map(record => record.accuracy);
        const wpmData = progressData.map(record => record.words_per_minute);
        const spmData = progressData.map(record => record.strokes_per_minute);

        const ctx = document.getElementById('performanceChart').getContext('2d');
        const performanceChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Accuracy (%)',
                        data: accuracyData,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        fill: false,
                    },
                    {
                        label: 'Words Per Minute',
                        data: wpmData,
                        borderColor: 'rgba(54, 162, 235, 1)',
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        fill: false,
                    },
                    {
                        label: 'Strokes Per Minute',
                        data: spmData,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        fill: false,
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Exercises'
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Metrics'
                        }
                    }
                }
            }
        });
});
