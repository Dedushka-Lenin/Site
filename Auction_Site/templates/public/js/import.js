function readTextFile(file, place) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                var allText = rawFile.responseText;
                document.querySelector(place).innerHTML = allText;
            }
        }
    };
    rawFile.send(null);
}

// export function readTextFile(file, place) {
//     var rawFile = new XMLHttpRequest();
//     rawFile.open("GET", file, false);
//     rawFile.onreadystatechange = function () {
//         if (rawFile.readyState === 4) {
//             if (rawFile.status === 200 || rawFile.status == 0) {
//                 var allText = rawFile.responseText;
//                 document.querySelector(place).innerHTML = allText;

//                 console.log(place);
//             }
//         }
//     };
//     rawFile.send(null);
// }
