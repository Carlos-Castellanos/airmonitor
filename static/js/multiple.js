const labels = ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05", "2021-01-06", "2021-01-07", "2021-01-08", "2021-01-09", "2021-01-10",];
console.log({ totaltemperatura })
console.log(labels)

let dates = totaldates;
//let dates = Label_Seconds;
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
            },
            x: {
                type: 'time',
                time: {
                    unit: 'day'
                }
            }

        },
    }
});


function filterDate() {
    const start1 = new Date(document.getElementById('start').value);
    const start = start1.setHours(0, 0, 0, 0)
    const end1 = new Date(document.getElementById('end').value);
    const end = end1.setHours(0, 0, 0, 0)
    const ss = start + 144000000;
    const filterDates = dates.filter(date => date >= (start + 144000000) && date <= (end + 144000000));
    console.log(start)
    console.log(end)
    console.log(filterDates)
    myChart.config.data.labels = filterDates;
    myChart.update();
};

function resetDate() {
    myChart.config.data.labels = dates;
    myChart.update();
}

function init() {
    //hook events, triggeres events
    console.log("init");
    document.getElementById("btnFilter").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("btnFilter");
        filterDate();

    });
    document.getElementById("btnReset").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("btnReset");
        resetDate();

    });

}

window.onpageshow = function () {
    console.log("algo");
};
window.onload = init;

