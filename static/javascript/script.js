// Resize all brand cards into squares by setting the height to equal the width.
squarify = () =>{
    var cardList = document.getElementsByClassName('card');
    for (var i = 0; i < cardList.length; i++ ) {
        var cardWidth = $(cardList[i]).width();
        $(cardList[i]).css({'height':cardWidth+'px'});
    }
}

// Squarify to set the intial size of the cards.
window.onload = () =>{
    squarify();
}

// Squarify every time the window is resized.
window.onresize = () =>{
    squarify();
}

// shortify = () =>{
//     textList = document.getElementsByClassName("preview-text");
//     console.log(list)
//     // para.innerText = para.innerText.substr(0, 100) + '...';
//     var i;
//     for (i = 0; i < list.length; i++) {
//         console.log("hello")
//     }
// }

// shortify();