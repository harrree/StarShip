      // Function to open the modal
      function openModal() {
        document.getElementById("editModal").style.display = "flex";
      }

      // Function to close the modal
      function closeModal() {
        document.getElementById("editModal").style.display = "none";
      }

      // Function to save changes
      function saveChanges() {
        const newUsername = document.getElementById("new-username").value;
        const newImage = document.getElementById("new-image").files[0];

        if (newUsername) {
          document.getElementById("username").textContent = newUsername;
          document.getElementById("display-username").textContent = newUsername;
        }

        if (newImage) {
          const reader = new FileReader();
          reader.onload = function (e) {
            document.getElementById("profile-image").src = e.target.result;
          };
          reader.readAsDataURL(newImage);
        }

        closeModal();
      }
      function openWatchlist() {
    document.getElementById("watchlistModal").style.display = "flex";
  }

  function closeWatchlist() {
    document.getElementById("watchlistModal").style.display = "none";
  }

  function openReviewed() {
    document.getElementById("reviewedModal").style.display = "flex";
  }
  let currentSlide = 0;

      function showSlide(index) {
        const slides = document.querySelector('.slides');
        const totalSlides = document.querySelectorAll('.slide').length;
        if (index >= totalSlides) {
          currentSlide = 0;
        } else if (index < 0) {
          currentSlide = totalSlides - 1;
        } else {
          currentSlide = index;
        }
        slides.style.transform = `translateX(${-currentSlide * 100}%)`;
      }
      function nextSlide() {
        showSlide(currentSlide + 1);
      }
      function prevSlide() {
        showSlide(currentSlide - 1);
      }
      // Initialize the first slide
      showSlide(currentSlide);
  function closeReviewed() {
    document.getElementById("reviewedModal").style.display = "none";
  }