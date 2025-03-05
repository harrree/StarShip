document.addEventListener("DOMContentLoaded", function () {
    /* ---- Auto-Sliding Posters ---- */
    let posters = document.querySelectorAll(".poster");
    let index = 0;

    function showNextPoster() {
        posters[index].classList.remove("active");
        index = (index + 1) % posters.length;
        posters[index].classList.add("active");
    }

    setInterval(showNextPoster, 5000); // Change poster every 5 seconds

    /* ---- Carousel Controls ---- */
    const carousel = document.querySelector(".carousel");
    let currentIndex = 0;

    function moveSlide(direction) {
        const totalItems = 10;
        const itemsPerSlide = 5;
        const maxIndex = Math.ceil(totalItems / itemsPerSlide) - 1;

        currentIndex += direction;

        if (currentIndex < 0) {
            currentIndex = maxIndex;
        } else if (currentIndex > maxIndex) {
            currentIndex = 0;
        }

        const translateX = -currentIndex * 100;
        carousel.style.transform = `translateX(${translateX}%)`;
    }

    document.querySelector(".prev").addEventListener("click", function () {
        moveSlide(-1);
    });

    document.querySelector(".next").addEventListener("click", function () {
        moveSlide(1);
    });
});
