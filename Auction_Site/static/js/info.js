var p_url = location.search.substring(1);

var parametr = p_url.split("&");

let values = new Array();
for (i in parametr) {
    var j = parametr[i].split("=");
    values[j[0]] = unescape(j[1]);
}

readTextFile(`../static/info/${values.path}.html`, ".info");

links = [login_button, register_button];

for (let elem of links) {
    elem.value = values.path;
}

/*----------------------------------------------------------------------------*/

links = ["About_Us", "Projects", "Terms_of_use"];

for (let elem of links) {
    for (let item of document.getElementsByClassName(elem)) {
        item.href = `?path=${elem}`;
    }
}
