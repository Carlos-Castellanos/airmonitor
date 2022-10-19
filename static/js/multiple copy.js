const labels = ["Enero", "febrero", "Marzo", "Abril", "Mayo", "Junio"];

let fechs = fechamediciones;
let temp = totaltemperatura;
let hum = totalhumedad;
let pres = totalpresio;
let pm25 = totalpm25;
let pm10 = totalpm10;

let ctx = document.getElementById("myChart").getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Temperature',
            data: temp,
            borderColor: 'rgba(252, 44, 3)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y',
        },
        {
            label: 'Humidity',
            data: hum,
            borderColor: 'rgba(3, 24, 252)',
            backgroundColor: 'rgba(3, 24, 252, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y1',
        },
        {
            label: 'Pression',
            data: pres,
            borderColor: 'rgba(94, 214, 47)',
            backgroundColor: 'rgba(94, 214, 47, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y2',
        },
        {
            label: 'PM 2.5',
            data: pm25,
            borderColor: 'rgba(47, 214, 169)',
            backgroundColor: 'rgba(47, 214, 169, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y3',
        },
        {
            label: 'PM 10',
            data: pm10,
            borderColor: 'rgba(147, 47, 214)',
            backgroundColor: 'rgba(147, 47, 214, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y4',
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
            },
            y2: {
                type: 'linear',
                display: true,
                position: 'right',
            },
            y3: {
                type: 'linear',
                display: true,
                position: 'right',
            },
            y4: {
                type: 'linear',
                display: true,
                position: 'right',
            }
        },
    }
});