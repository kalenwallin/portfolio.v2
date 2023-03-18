const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".hide", {
    x: "0%",
    duration: 0.3,
    opacity: 1,
});

tl.to(".preloader", { opacity: 1, duration: 0 });

var $intro = $(".preloader"),
    $items = $intro.find(".item"),
    itemsLen = $items.length,
    svgs = $intro.find("svg").drawsvg({
        reverse: true,
        easing: "easeOutQuart",
        callback: animateIntro,
    }),
    currItem = 0;

function animateIntro() {
    $items
        .removeClass("active")
        .eq(currItem++ % itemsLen)
        .addClass("active")
        .find("svg")
        .drawsvg("animate");
}

function animateIntro() {
    $items
        .removeClass("active")
        .eq(currItem++ % itemsLen)
        .addClass("active")
        .find("svg")
        .drawsvg("animate");
}

animateIntro();

tl.to(".to-animate", {
    opacity: 0,
    duration: 0,
});
tl.to(".to-animate-line", {
    opacity: 0,
    duration: 0,
});
tl.to(".svg-line", {
    opacity: 0,
    duration: 0,
});

imagesLoaded("body", { background: true }, function () {
    tl.to(".preloader", {
        opacity: 0,
        duration: 0.6,
        onComplete: () => {
            // headings and buttons
            elements = document.querySelectorAll(".to-animate");
            elements.forEach((e) => {
                e.classList.remove("to-animate");
                e.classList.add("slide-in-from-top-header");
            });
            // lines
            elements = document.querySelectorAll(".to-animate-line");
            elements.forEach((e) => {
                e.classList.remove("to-animate-line");
                e.classList.add("hero-line-vertical");
            });
            // hero lines
            var hero = $(".line-container svg").drawsvg();
            hero.drawsvg("animate");
        },
    });
    tl.to(".svg-line", {
        opacity: 1,
        duration: 0,
    });
    tl.to(".to-animate-line", {
        opacity: 1,
        duration: 0,
    });
    tl.set(".preloader", {
        zIndex: 0,
        duration: 0,
    });
});
