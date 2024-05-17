var p_url = location.search.substring(1);

var parametr = p_url.split("&");

let values = new Array();
for (i in parametr) {
    var j = parametr[i].split("=");
    values[j[0]] = unescape(j[1]);
}

readTextFile(`../static/info/${values.path}.html`, ".info");

for (let elem of document.getElementsByClassName('login_button_close')) {
    elem.name = "path"
    elem.value = values.path;
}