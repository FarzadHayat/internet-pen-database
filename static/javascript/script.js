// Calculates the number of navbar links in the header
navbar = () =>{
    const navItems = $('nav a').length;
    const body = $('body');
    body.css({'--navbar-items': navItems});
}

// Resize all brand cards into squares by setting the height to equal the width.
squarify = () =>{
    var cardList = document.getElementsByClassName('card');
    if(cardList != null){
        for(var i = 0; i < cardList.length; i++){
            var cardWidth = $(cardList[i]).width();
            $(cardList[i]).css({'height': cardWidth+'px'});
        }   
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
    var homeLink = $('#homelink');
    var searchLink = $('#searchlink');
    
    
    const urlPath = window.location.pathname;
    
    // if user is on the home aka. slanding page
    if(urlPath == "/"){
        // highlight
        homeLink.addClass('active');
        homeLink.siblings().removeClass('active');
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
                    searchLink.removeClass('active');
                }
                // Debug
                // console.log(this.hash, "Scroll bar location: ", scrollBarLocation)
                // console.log(this.hash, "Section offset: ", sectionOffset)
            })
        })
    }
    if(urlPath == "/search"){
        searchLink.addClass('active');
        searchLink.siblings().removeClass('active');
    }
})

// Shorten brand card description length and end with a ...
shortify = () =>{
    const descriptionList = $('.card-info .description');
    const length = 140;
    if(descriptionList != null){
        for(var i = 0; i < descriptionList.length; i++){
            if(descriptionList[i].innerText.length > length){
                descriptionList[i].innerText = descriptionList[i].innerText.substr(0, length) + '...';
            }
        }
    }
}

// carousel slideshow
var slideshow;
var slides;
var counter;
var size;

slideshow = () =>{
    // parents with grid property
    slideshow = document.querySelector('#slideshow');
    if(slideshow == null){
        return;
    }
    // get list of all slide divs
    slides = document.querySelectorAll('.slide');
    // console.log("Slide length: " + slides.length);
    
    // Buttons
    const prevButton = document.querySelector('#prev-button');
    const nextButton = document.querySelector('#next-button');
    
    // Counter
    counter = 1;
    size = slideshow.clientWidth;

    slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';

    // Button Listeners
    nextButton.addEventListener('click', ()=>{
        if(counter >= slides.length - 1) return;
        slideshow.style.transition = "transform 0.4s ease-in-out";
        counter++;
        slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';
        // console.log("User clicked next | Counter: " + counter);
    });

    prevButton.addEventListener('click', ()=>{
        if(counter <= 0) return;
        slideshow.style.transition = "transform 0.4s ease-in-out";
        counter--;
        slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';
        // console.log("User clicked prev | Counter: " + counter);
    });

    // Slideshow Listeners
    slideshow.addEventListener('transitionend', ()=>{
        // Create loop at the start that goes back to the last slide (clone of last slide at the start)
        if(slides[counter].id ===  'lastClone'){
            slideshow.style.transition = "none";
            counter = slides.length - 2;
            slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';
            // console.log("Landed on first slide, going back to lastClone | Counter: " + counter);
        }
        // Create loop at the end that goes back to the first slide (clone of first slide at the end)
        if(slides[counter].id ===  'firstClone'){
            slideshow.style.transition = "none";
            counter = slides.length - counter;
            slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';
            // console.log("Landed on last slide, going back to firstClone | Counter: " + counter);
        }    
    });
    
}

slideshowResize = () =>{
    if(slideshow == null){
        return;
    }
    size = slideshow.clientWidth;
    slideshow.style.transition = "none";
    slideshow.style.transform = 'translateX(' + (-size * counter) + 'px)';
}

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