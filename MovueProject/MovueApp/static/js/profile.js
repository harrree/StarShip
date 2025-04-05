// profile.js

function EditProfile() {
  const modal = document.getElementById("editProfileModal");
  modal.style.display = "flex"; // Using flex instead of block for better centering
}

function closeEditProfile() {   
  document.getElementById("editProfileModal").style.display = "none";
}

// Add event listeners when the DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
  // Make sure the Edit Profile button works
  const editBtn = document.querySelector(".edit-btn");
  if (editBtn) {
    editBtn.addEventListener("click", EditProfile);
  }
  
  // Make sure the Cancel button works in the modal
  const closeBtn = document.querySelector(".close-btn");
  if (closeBtn) {
    closeBtn.addEventListener("click", closeEditProfile);
  }
  
  // Close modal when clicking outside the modal content
  const modal = document.getElementById("editProfileModal");
  if (modal) {
    modal.addEventListener("click", function(event) {
      if (event.target === modal) {
        closeEditProfile();
      }
    });
  }
});