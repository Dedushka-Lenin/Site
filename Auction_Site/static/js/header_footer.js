// import readTextFile from "import.js";

readTextFile("../static/auxiliary/header.html", "header");
readTextFile("../static/auxiliary/footer.html", "footer");

readTextFile("../static/auxiliary/dialogue.html", "main .dialogue");

/*----------------------------------------------------------------------------*/

links = ["About_Us", "Projects", "Terms_of_use"];

for (let elem of links) {
    for (let item of document.getElementsByClassName(elem)) {
        item.href = `../info?path=${elem}`;
    }
}

/*----------------------------------------------------------------------------*/

let navToggle = document.querySelector(".nav__toggle");
let navWrapper = document.querySelector(".nav__wrapper");

navToggle.addEventListener("click", function () {
    if (navWrapper.classList.contains("active")) {
        this.setAttribute("aria-expanded", "false");
        this.setAttribute("aria-label", "menu");
        navWrapper.classList.remove("active");
    } else {
        navWrapper.classList.add("active");
        this.setAttribute("aria-label", "close menu");
        this.setAttribute("aria-expanded", "true");
    }
});