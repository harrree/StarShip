  
  
  function EditProfile() {
    console.log("EditProfile function is running");
    var modal = document.getElementById("editProfileModal");
    modal.style.display = "block";
  }

  function closeEditProfile() {   
     document.getElementById("editProfileModal").style.display = "none";
  }

// function prevSlide(type) {
//    const carousel = document.querySelector(`.${type} .carousel`);
//    carousel.scrollBy({ left: -200, behavior: "smooth" });
//  }

//  function nextSlide(type) {
//    const carousel = document.querySelector(`.${type} .carousel`);
//    carousel.scrollBy({ left: 200, behavior: "smooth" });
//  }

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
