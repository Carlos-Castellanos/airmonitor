function get_year(page) {

    var periodo = document.getElementById("periodo");
    var vPP = periodo.options[periodo.selectedIndex].value;
    console.log(page)
    // "/" + page + "/";

    switch (vPP) {

        case "2":
            document.getElementById("anyo").selectedIndex = 0;
            document.getElementById("mes").selectedIndex = 0;
            document.getElementById("anyo").style.display = 'none';
            document.getElementById("mes").style.display = 'none';
            document.getElementById("ldia").style.display = 'block';
            var dia = document.getElementById("dia");
            var vDD = dia.value;
            myURL = "/sensors/" + vDD + "/" + page + "/";

            break;
        case "1":
            document.getElementById("dia").selectedIndex = 0;
            document.getElementById("dia").value = "";
            document.getElementById("anyo").style.display = 'block';
            document.getElementById("mes").style.display = 'block';
            document.getElementById("ldia").style.display = 'none';
            var anyo = document.getElementById("anyo");
            var vYY = anyo.options[anyo.selectedIndex].value;
            var mes = document.getElementById("mes");
            var vMM = mes.options[mes.selectedIndex].value;
            myURL = "/sensors/" + vYY + "-" + vMM + "-0" + "/" + page + "/";
            break;
        case "0":
            document.getElementById("mes").selectedIndex = 0;
            document.getElementById("dia").selectedIndex = 0;
            document.getElementById("dia").value = "";
            document.getElementById("anyo").style.display = 'block';
            document.getElementById("mes").style.display = 'none';
            document.getElementById("ldia").style.display = 'none';
            var anyo = document.getElementById("anyo");
            var vYY = anyo.options[anyo.selectedIndex].value;
            myURL = "/sensors/" + vYY + "-0-0" + "/" + page + "/";
            break;

    }

    //document.getElementById('test').innerHTML = myURL;
    document.getElementById('bChange').setAttribute('href', myURL);
    return vYY;
}




function init() {
    console.log("init");
    document.getElementById("mes").selectedIndex = 0;
    document.getElementById("dia").value = "";
    document.getElementById("anyo").style.display = 'block';
    document.getElementById("mes").style.display = 'none';
    document.getElementById("ldia").style.display = 'none';

    // document.getElementById("anyo").addEventListener("change", function (event) {
    //     event.preventDefault();
    //     console.log("anyo");
    //     get_year('maps');
    // });

}


window.onload = init;