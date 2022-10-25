const ctx = document.getElementById('myChart').getContext('2d');
const dates = ['2021-11-01', '2021-11-02', '2021-11-03', '2021-11-04', '2021-11-05', '2021-11-06', '2021-11-07'];
console.log('2021-11-01');
const datapoints = [12, 19, 3, 5, 2, 3, 6];
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        //            labels: [{% for item in qs %} '{{item.measurementDate}}', {% endfor %}],
        labels: dates,
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3, 6],
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1
        }]
    },

    options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'day'
                }
            }
        }
    }
});

