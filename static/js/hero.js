function adjustObjectSize() {
    const object = document.getElementById("animated-svg");
    const windowAspectRatio = window.innerWidth / window.innerHeight;
    const objectAspectRatio = 4000 / 2295; // Change this to the aspect ratio of your animated SVG

    if (windowAspectRatio >= objectAspectRatio) {
        object.style.width = "100%";
        object.style.height = "auto";
    } else {
        object.style.width = "auto";
        object.style.height = "100vh";
    }

    object.style.opacity = "1"; // Show the SVG after the size is adjusted
}

// Initially set the size of the object
window.addEventListener("load", adjustObjectSize);

// Update the size of the object whenever window is resized
window.addEventListener("resize", adjustObjectSize);
