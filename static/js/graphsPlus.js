const ctx = document.getElementById('myChart').getContext('2d');

const zoomOptions = {
    pan: {
        enabled: true,
        modifierKey: 'ctrl',
    },
    zoom: {
        drag: {
            enabled: true
        },
        mode: 'xy',
    },
};
// </block>

const panStatus = () => zoomOptions.pan.enabled ? 'enabled' : 'disabled';
const zoomStatus = () => zoomOptions.zoom.drag.enabled ? 'enabled' : 'disabled';



const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            // x: {
            //     position: 'bottom',
            //     // type: 'time',
            //     ticks: {
            //         autoSkip: true,
            //         autoSkipPadding: 50,
            //         maxRotation: 0
            //     },
            //     // time: {
            //     //     displayFormats: {
            //     //         hour: 'HH:mm',
            //     //         minute: 'HH:mm',
            //     //         second: 'HH:mm:ss'
            //     //     }
            //     // }
            // },
            // y: {
            //     position: 'right',
            //     ticks: {
            //         callback: (val, index, ticks) => index === 0 || index === ticks.length - 1 ? null : val,
            //     },
            //     grid: {
            //         borderColor: Utils.randomColor(1),
            //         color: 'rgba( 0, 0, 0, 0.1)',
            //     },
            //     title: {
            //         display: true,
            //         text: (ctx) => ctx.scale.axis + ' axis',
            //     }
            // },
        },

        plugins: {
            zoom: zoomOptions,
            title: {
                display: true,
                position: 'bottom',
                text: (ctx) => 'Zoom: ' + zoomStatus() + ', Pan: ' + panStatus()
            }
        },
    }
});





