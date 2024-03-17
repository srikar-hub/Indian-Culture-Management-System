// References to DOM Elements
const prevBtn = document.querySelector("#prev-btn");
const nextBtn = document.querySelector("#next-btn");
const book = document.querySelector("#book");

// Query all papers
const papers = document.querySelectorAll(".paper");

// Event Listener
prevBtn.addEventListener("click", goPrevPage);
nextBtn.addEventListener("click", goNextPage);

// Business Logic
let currentLocation = 1;
const maxLocation = papers.length + 1;

function openBook() {
    book.style.transform = "translateX(50%)";
    prevBtn.style.transform = "translateX(-180px)";
    nextBtn.style.transform = "translateX(180px)";
}

function closeBook(isAtBeginning) {
    if (isAtBeginning) {
        book.style.transform = "translateX(0%)";
    } else {
        book.style.transform = "translateX(100%)";
    }

    prevBtn.style.transform = "translateX(0px)";
    nextBtn.style.transform = "translateX(0px)";
}

function updateZIndex() {
    papers.forEach((paper, index) => {
        const distanceFromCurrent = Math.abs(index - (currentLocation - 1));
        paper.style.zIndex = maxLocation - distanceFromCurrent;
    });
}


function goNextPage() {
    if (currentLocation < maxLocation) {
        openBook();
        papers[currentLocation - 1].classList.add("flipped");
        currentLocation++;
        updateZIndex();
        if (currentLocation === maxLocation) {
            closeBook(false);
        }
    }
}

function goPrevPage() {
    if (currentLocation > 1) {
        if (currentLocation === maxLocation) {
            openBook();
        }
        papers[currentLocation - 2].classList.remove("flipped");
        currentLocation--;
        updateZIndex();
        if (currentLocation === 1) {
            closeBook(true);
        }
    }
}

// Call updateZIndex initially to set the correct z-index
updateZIndex();