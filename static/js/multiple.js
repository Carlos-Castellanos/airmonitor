
let dates = totaldates;
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
            label: 'Temperature Celcius',
            data: temp,
            borderColor: 'rgba(252, 44, 3)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'Celcius',
        },
        {
            label: 'Humidity %',
            data: hum,
            borderColor: 'rgba(3, 24, 252)',
            backgroundColor: 'rgba(3, 24, 252, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: '%',
        },
        {
            label: 'Pressure kPa',
            data: pres,
            borderColor: 'rgba(147, 47, 214)',
            backgroundColor: 'rgba(147, 47, 214, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: 'kPa',
        },
        {
            type: 'bar',
            label: 'PM 2.5 µg/m3',
            data: pm25,
            borderColor: 'rgba(47, 214, 208)',
            backgroundColor: 'rgba(47, 214, 208, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: '2.5 µg/m3',
        },
        {
            type: 'bar',
            label: 'PM 10 µg/m3',
            data: pm10,
            borderColor: 'rgba(53, 214, 47)',
            backgroundColor: 'rgba(53, 214, 47, 0.2)',
            borderWidth: 1,
            hidden: false,
            yAxisID: '10 µg/m3',
        },
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        stacked: false,
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            x: {
                type: 'time',
                time: {
                    unit: 'day',
                },
                grid: {
                    color: 'red',
                    borderColor: 'blue',
                    tickColor: 'red'
                },
                ticks: {
                    color: 'blue',
                    stepSize: 1,
                    min: 0,
                    autoSkip: false
                },
                title: {
                    color: 'red',
                    display: true,
                    text: 'Days'
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Sensor Data'
            },
            zoom: {
                pan: {
                    enabled: false,
                    mode: 'x',
                },
                zoom: {
                    mode: 'x',
                    wheel: {
                        enabled: true,
                    },
                    pinch: {
                        enabled: true
                    },
                    drag: {
                        enabled: true,
                        backgroundColor: 'rgba(108, 122, 137, 0.3)', //this color is called Lynch
                    },
                    mode: 'x',
                }
            }
        }
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



function periodicity(event) {
    if (event.target.value === "0") {
        console.log("here 0");
        myChart.config.data.labels = totaldates;
        myChart.data.datasets[0].data = totaltemperatura;
        myChart.data.datasets[1].data = totalhumedad;
        myChart.data.datasets[2].data = totalpresion;
        myChart.data.datasets[3].data = totalpm25;
        myChart.data.datasets[4].data = totalpm10;
        myChart.config.options.scales.x.time.unit = 'day';
        myChart.config.options.scales.x.title.text = 'DAYS';
        console.log(myChart.config.data.datasets[0].data)
        myChart.update();


    }
    else if (event.target.value === "3") {
        console.log("here 3");
        myChart.config.data.labels = monthlydates;
        myChart.config.data.datasets[0].data = monthlytemperatura;
        myChart.config.data.datasets[1].data = monthlyhumedad;
        myChart.config.data.datasets[2].data = monthlypresion;
        myChart.config.data.datasets[3].data = monthlypm25;
        myChart.config.data.datasets[4].data = monthlypm10;
        myChart.config.options.scales.x.time.unit = 'month';
        myChart.config.options.scales.x.title.text = 'MONTHS';
        console.log(myChart.config.data.datasets[0].data)
        myChart.update();
    }

    else if (event.target.value === "9") {
        console.log("here 9");
        myChart.config.data.labels = yearlydates;
        myChart.config.data.datasets[0].data = yearlytemperatura;
        myChart.config.data.datasets[1].data = yearlyhumedad;
        myChart.config.data.datasets[2].data = yearlypresion;
        myChart.config.data.datasets[3].data = yearlypm25;
        myChart.config.data.datasets[4].data = yearlypm10;
        myChart.config.options.scales.x.time.unit = 'year';
        myChart.config.options.scales.x.title.text = 'YEARS';
        console.log("labels")
        console.log(myChart.config.data.labels)
        console.log(yearlydates)
        console.log("temperatura")
        console.log(myChart.config.data.datasets[0].data)
        myChart.update();
    }

};


function resetDate() {
    myChart.config.data.labels = dates;
    myChart.update();
    graphZoomReset()

}

function graphZoomReset() {
    myChart.resetZoom();
    console.log("zoom reset")
    myChart.config.data.labels = totaldates;
    myChart.data.datasets[0].data = totaltemperatura;
    myChart.data.datasets[1].data = totalhumedad;
    myChart.data.datasets[2].data = totalpresion;
    myChart.data.datasets[3].data = totalpm25;
    myChart.data.datasets[4].data = totalpm10;
    myChart.config.options.scales.x.time.unit = 'day';
    myChart.config.options.scales.x.title.text = 'DAYS';
    console.log(myChart.config.data.datasets[0].data)
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
        resetDate();
        console.log("first reset");


    });



    document.getElementById("listPeriodicity").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("listPeriodicity");
        periodicity(event);

    });
}

window.onpageshow = function () {
    console.log("algo");
};
window.onload = init;
