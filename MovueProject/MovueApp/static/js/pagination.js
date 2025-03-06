let currentPage = 1;
const totalPages = 2;

function changePage(direction) {
    currentPage += direction;

    if (currentPage < 1) currentPage = totalPages;
    if (currentPage > totalPages) currentPage = 1;

    document.getElementById("page-number").textContent = currentPage;
}
