const labels = ["Enero", "febrero", "Marzo", "Abril", "Mayo", "Junio"];
//let temp = {{total_temperatura|safe}}
let ctx = document.getElementById("myChart").getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Temperature!!!!',
            data: [12, 19, 3, 5, 2, 3],
            //           data: temp,
            borderColor: 'rgba(252, 44, 3)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y',
        },
        {
            label: 'Humedad',
            data: [22, 29, 33, 55, 52, 33],
            borderColor: 'rgba(3, 24, 252)',
            backgroundColor: 'rgba(3, 24, 252, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y1',
        },
        ]
    },
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        stacked: false,
        plugins: {
            title: {
                display: true,
                text: 'Chart.js Line Chart - Multi Axis'
            }
        },
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',
            }
        },
    }
});