document.addEventListener("DOMContentLoaded", function () {
    const profileBtn = document.getElementById("profile-btn");
    const dropdownContent = document.getElementById("dropdown-content");

    // Toggle dropdown on click
    profileBtn.addEventListener("click", function () {
        dropdownContent.classList.toggle("show");
    });

    // Close dropdown if clicked outside
    document.addEventListener("click", function (event) {
        if (!profileBtn.contains(event.target) && !dropdownContent.contains(event.target)) {
            dropdownContent.classList.remove("show");
        }
    });
});
