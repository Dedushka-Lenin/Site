var p_url = location.search.substring(1);

var parametr = p_url.split("&");

let values = new Array();
for (i in parametr) {
    var j = parametr[i].split("=");
    values[j[0]] = unescape(j[1]);
}

readTextFile(`public/info/${values.path}.html`, ".info");

links = [login_button, register_button];

for (let elem of links) {
    elem.value = values.path;
}
