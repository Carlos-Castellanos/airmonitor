const labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];

console.log({ totaltemperatura })
console.log(labels)

let dates = fechamediciones;
let temp = totaltemperatura;
let hum = totalhumedad;
let pres = totalpresion;
let pm25 = totalpm25;
let pm10 = totalpm10;

let ctx = document.getElementById("myChart").getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
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
            yAxisID: 'y',
        },
        {
            label: 'Pression',
            data: pres,
            borderColor: 'rgba(147, 47, 214)',
            backgroundColor: 'rgba(147, 47, 214, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y',
        },
        {
            label: 'PM 2.5',
            data: pm25,
            borderColor: 'rgba(47, 214, 208)',
            backgroundColor: 'rgba(47, 214, 208, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y',
        },
        {
            label: 'PM 10',
            data: pm10,
            borderColor: 'rgba(53, 214, 47)',
            backgroundColor: 'rgba(53, 214, 47, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'y',
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
            }

        },
    }
});