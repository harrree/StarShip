document.getElementById("change-profile").addEventListener("click", function () {
    document.getElementById("file-input").click();
  });
  
  document.getElementById("file-input").addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById("profile-pic").src = e.target.result;
            localStorage.setItem("profileImage", e.target.result); // Store in localStorage
        };
        reader.readAsDataURL(file);
    }
  });
  
  // Load saved profile image on page load
  window.onload = function () {
    const savedImage = localStorage.getItem("profileImage");
    if (savedImage) {
        document.getElementById("profile-pic").src = savedImage;
    }
  };
  
  // Button navigation
  document.getElementById("reviewed-movies").addEventListener("click", function () {
    window.location.href = "/reviewed-movies"; // Update with actual URL in Django
  });
  
  document.getElementById("watchlist").addEventListener("click", function () {
    window.location.href = "/watchlist"; // Update with actual URL in Django
  });