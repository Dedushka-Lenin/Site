function delete_class(button) {
    document
        .querySelector(`main .list_button ${button}`)
        .classList.add("active");

    document
        .querySelector(`main .info ${button}`)
        .classList.remove("display_none");

    for (let elem of list_button) {
        if (elem != button) {
            document
                .querySelector(`main .list_button ${elem}`)
                .classList.remove("active");

            document
                .querySelector(`main .info ${elem}`)
                .classList.add("display_none");
        }
    }
}

list_button = [".description", ".peculiarities", ".reviews"];

for (let elem of list_button) {
    document
        .querySelector(`main .list_button ${elem}`)
        .addEventListener("click", function () {
            delete_class(elem);
        });
}

/*----------------------------------------------------------------------------*/

links = ["About_Us", "Projects", "Terms_of_use"];

for (let elem of links) {
    for (let item of document.getElementsByClassName(elem)) {
        item.href = `info?path=${elem}`;
    }
}

/*----------------------------------------------------------------------------*/

function triggerDownload(fileName) {
    var element = document.createElement("a");
    element.setAttribute("href", fileName);
    element.setAttribute("download", fileName);
    element.style.display = "none";
    document.body.appendChild(element);
    // Происходит клик, словно совершил его сам программирующий ниндзя
    element.click();
    document.body.removeChild(element);
}
