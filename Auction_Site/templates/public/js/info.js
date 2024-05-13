var p_url = location.search.substring(1);

var parametr = p_url.split("&");

let values = new Array();
for (i in parametr) {
    var j = parametr[i].split("=");
    values[j[0]] = unescape(j[1]);
}

let myHeading = document.querySelector(".info");

function readTextFile(file) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                var allText = rawFile.responseText;
                myHeading.innerHTML = allText;
            }
        }
    };
    rawFile.send(null);
}

readTextFile(`public/info/${values.path}.html`);

links = [login_button, register_button];

for (let elem of links) {
    elem.value = values.path;
}
