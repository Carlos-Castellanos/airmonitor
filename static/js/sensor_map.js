function get_year() {
    x = document.getElementsByName("anyo").values;
    document.getElementById('test').innerHTML = document.getElementsByName("anyo").values;
    var anyo = document.getElementById("anyo");
    var pro = anyo.options[anyo.selectedIndex].value;
    //Creamos un nodo de texto que agregaremos al div.
    //myURL = "{%  url 'show_map' yy=" + pro + "%}";
    myURL = "/sensors/" + pro + "/maps/";
    document.getElementById('test').innerHTML = myURL;
    document.getElementById('bChange').setAttribute('href', myURL);
    return pro;
}

