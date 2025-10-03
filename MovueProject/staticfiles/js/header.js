document.addEventListener("DOMContentLoaded", function () {
    const profileBtn = document.getElementById("profile-btn");
    const dropdownContent = document.getElementById("dropdown-content");
    const genreBtn = document.getElementById("genre-btn");
    const genreMenu = document.getElementById("genre-menu");

    // Toggle profile dropdown
    profileBtn?.addEventListener("click", function (e) {
        e.stopPropagation();
        dropdownContent.classList.toggle("show");
        genreMenu?.classList.remove("show");
    });

    // Toggle genre dropdown
    genreBtn?.addEventListener("click", function (e) {
        e.stopPropagation();
        genreMenu.classList.toggle("show");
        dropdownContent?.classList.remove("show");
    });

    // Close all dropdowns on outside click
    document.addEventListener("click", function (event) {
        if (!profileBtn?.contains(event.target)) {
            dropdownContent?.classList.remove("show");
        }
        if (!genreBtn?.contains(event.target)) {
            genreMenu?.classList.remove("show");
        }
    });
});
