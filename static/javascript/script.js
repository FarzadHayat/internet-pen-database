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

// Highlight anchor link
$(document).ready(function(){
    
    var navLink = $('.navlink');
    const bodyContainer = $('#main');
    
    $(bodyContainer).scroll(function(){
        // get location of scroll bar
        var scrollBarLocation = $(this).scrollTop();

        // get distance of scroll bar to each section
        navLink.each(function(){
            var sectionOffset = $(this.hash).offset().top;

            // highlight active link and un-highlight the rest
            if(sectionOffset <= scrollBarLocation){
                $(this).addClass('active');
                
                $(this).siblings().removeClass('active');
            }
        })
    })
})

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