document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll(".star");
    const ratingInput = document.getElementById("selected-rating");
    const reviewForm = document.getElementById("review-form");

    stars.forEach(star => {
        star.addEventListener("mouseover", function () {
            highlightStars(this.dataset.value);
        });

        star.addEventListener("mouseout", resetStars);

        star.addEventListener("click", function () {
            ratingInput.value = this.dataset.value;
        });
    });

    function highlightStars(value) {
        stars.forEach(star => {
            if (parseFloat(star.dataset.value) <= parseFloat(value)) {
                star.classList.add("full");
            } else {
                star.classList.remove("full");
            }
        });
    }

    function resetStars() {
        highlightStars(ratingInput.value);
    }

    reviewForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const rating = ratingInput.value;
        const reviewText = document.getElementById("review-text").value;
        const movieId = "{{ movies.id }}";

        if (!rating || rating < 0.5) {
            alert("Please select a rating.");
            return;
        }

        fetch(`/submit-rating/${movieId}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": "{{ csrf_token }}",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ rating: rating, review: reviewText })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Review submitted successfully!");
                location.reload();
            } else {
                alert("Error: " + data.error);
            }
        });
    });
});
