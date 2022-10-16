// var fechas = {{ fecha_contagios| safe}};
//var Temperature = {{ Temperature| safe}};
// var fallecidos = {{ total_fallecidos| safe}};
// var vacunados = {{ total_vacunados| safe}};

let miCanvas = document.getElementById('myChart').getContext("2d");


var chart = new Chart(miCanvas, {
    type: "line",
    data: {
        labels: fechas,
        datasets: [{
            data: Temperature,
            label: 'Temperature',
            barThickness: 'flex',
            backgroundColor: '#03a9fc',
        },
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
})

// var fechas;
// var estado;
// document.querySelector('.selector').addEventListener("change", changeText);

// function changeText(event) {
//     if (event.target.value === "contagiados") {
//         // console.log(1)
//         estado = contagiados;
//         NewLabel = 'Contagiados'
//         // console.log(estado);
//         // chart.labels.data = fechas
//         chart.data.datasets[0].data = estado
//         chart.data.datasets[0].label = NewLabel;
//         // var other = chart.data.datasets[0]
//         // console.log(chart.data.datasets)
//         chart.update();

//         document.getElementById('Total_fecha').innerHTML = 'Total contagios por fecha';

//     }
//     else if (event.target.value === "fallecidos") {
//         // console.log(2);
//         estado = fallecidos;
//         NewLabel = 'Fallecidos'
//         // console.log(estado);
//         // chart.labels.data = fechas
//         chart.data.datasets[0].data = estado;
//         chart.data.datasets[0].label = NewLabel;
//         // var other = chart.data.datasets[0]
//         // console.log(chart.data.datasets)
//         chart.update();

//         document.getElementById('Total_fecha').innerHTML = 'Total fallecidos por fecha';

//     }
//     else {
//         // console.log(3);
//         estado = vacunados;
//         NewLabel = 'Vacunados'
//         // console.log(estado);
//         // chart.labels.data = fechas
//         chart.data.datasets[0].data = estado;
//         chart.data.datasets[0].label = NewLabel;
//         // var other = chart.data.datasets[0]
//         // console.log(chart.data.datasets)
//         chart.update();

//         document.getElementById('Total_fecha').innerHTML = 'Total vacunados por fecha';

//     }
// }


