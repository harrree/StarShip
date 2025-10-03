document.addEventListener("DOMContentLoaded", function () {
    const carousels = document.querySelectorAll(".carousel-container");

    carousels.forEach(carouselContainer => {
        const carousel = carouselContainer.querySelector(".carousel");
        const prevBtn = carouselContainer.querySelector(".prev");
        const nextBtn = carouselContainer.querySelector(".next");

        let scrollAmount = 0;
        const scrollStep = carousel.clientWidth / 2;

        prevBtn.addEventListener("click", () => {
            scrollAmount -= scrollStep;
            if (scrollAmount < 0) scrollAmount = 0;
            carousel.style.transform = `translateX(-${scrollAmount}px)`;
        });

        nextBtn.addEventListener("click", () => {
            scrollAmount += scrollStep;
            if (scrollAmount > carousel.scrollWidth - carousel.clientWidth) {
                scrollAmount = carousel.scrollWidth - carousel.clientWidth;
            }
            carousel.style.transform = `translateX(-${scrollAmount}px)`;
        });
    });
});
