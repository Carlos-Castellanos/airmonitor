function colorPM10() {
    if (pm_10 < 54) {
        document.getElementById("fpm10").style.backgroundColor = "#03fc4e";
    } else if (pm_10 < 154) {
        document.getElementById("fpm10").style.backgroundColor = "#4d66b8";
    } else if (pm_10 < 254) {
        document.getElementById("fpm10").style.backgroundColor = "#eef20a";
    } else if (pm_10 < 354) {
        document.getElementById("fpm10").style.backgroundColor = "#dbbd4f";
    }
    else {
        document.getElementById("fpm10").style.backgroundColor = "#6e0a0a";
    }

}
function colorPM25() {
    if (pm_25 < 8.9) {
        document.getElementById("fpm25").style.backgroundColor = "#03fc4e";
    } else if (pm_25 < 25.9) {
        document.getElementById("fpm25").style.backgroundColor = "#4d66b8";
    } else if (pm_25 < 39.9) {
        document.getElementById("fpm25").style.backgroundColor = "#eef20a";
    } else if (pm_25 < 106.9) {
        document.getElementById("fpm25").style.backgroundColor = "#dbbd4f";
    } else if (pm_25 < 177.9) {
        document.getElementById("fpm25").style.backgroundColor = "#db774f";
    } else if (pm_25 < 250) {
        document.getElementById("fpm25").style.backgroundColor = "#d41919";
    }
    else {
        document.getElementById("fpm25").style.backgroundColor = "#6e0a0a";
    }

}

function colorTemp() {
    if (temp < 20) {
        document.getElementById("ftemp").style.backgroundColor = "#0af2f2";
    } else if (temp < 32) {
        document.getElementById("ftemp").style.backgroundColor = "#0af240";
    }
    else {
        document.getElementById("ftemp").style.backgroundColor = "#f20a0a";
    }

}


function init() {
    colorTemp();
    colorPM25();
    colorPM10();
}

window.onload = init;

