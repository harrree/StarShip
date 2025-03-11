function openEditProfile() {
  document.getElementById("editProfileModal").style.display = "flex";
}

function closeEditProfile() {
  document.getElementById("editProfileModal").style.display = "none";
}

function prevSlide(type) {
  const carousel = document.querySelector(`.${type} .carousel`);
  carousel.scrollBy({ left: -200, behavior: "smooth" });
}

function nextSlide(type) {
  const carousel = document.querySelector(`.${type} .carousel`);
  carousel.scrollBy({ left: 200, behavior: "smooth" });
}
