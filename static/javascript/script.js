// Calculates the number of navbar links in the header
navbar = () =>{
    const navItems = $('nav a').length;
    const body = $('body');
    body.css({'--navbar-items': navItems});
}

// Resize all brand cards into squares by setting the height to equal the width.
squarify = () =>{
    var cardList = document.getElementsByClassName('card');
    for(var i = 0; i < cardList.length; i++){
        var cardWidth = $(cardList[i]).width();
        $(cardList[i]).css({'height': cardWidth+'px'});
    }
}

// Flip brand card on click
flip = (cardContent) =>{
    // Flip
    if(cardContent.style.transform == ''){
        cardContent.style.transform = 'rotateY(180deg)';
    }
    else{
        // Unflip
        if(cardContent.style.transform == 'rotateY(180deg)'){
            cardContent.style.transform = '';
        }
    }
}

// Highlight anchor link
$(document).ready(function(){
    
    var navLink = $('.navlink');
    const main = $('#main');

    $(main).scroll(function(){
        // get location of scroll bar
        var scrollBarLocation = $(this).scrollTop();

        // get distance of scroll bar to each section
        navLink.each(function(){
            var sectionOffset = $(this.hash).offset().top + scrollBarLocation - 200;

            // highlight active link and un-highlight the rest
            if(sectionOffset <= scrollBarLocation){
                $(this).addClass('active');
                $(this).siblings().removeClass('active');
            }
            // Debug
            // console.log(this.hash, "Scroll bar location: ", scrollBarLocation)
            // console.log(this.hash, "Section offset: ", sectionOffset)
        })
    })
})

// Shorten brand card description length and end with a ...
shortify = () =>{
    const descriptionList = $('.card-info .description');
    const length = 140;
    for(var i = 0; i < descriptionList.length; i++){
        if(descriptionList[i].innerText.length > length){
            descriptionList[i].innerText = descriptionList[i].innerText.substr(0, length) + '...';
        }
    }
}

// shortify();

// Squarify to set the intial size of the cards.
window.onload = () =>{
    squarify();
    navbar();
    shortify();
    slideshow();
}

// Squarify every time the window is resized.
window.onresize = () =>{
    squarify();
    shortify();
    slideshowResize();
}