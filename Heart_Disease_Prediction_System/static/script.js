var modal = document.querySelector(".modal");
var closeButton = document.querySelector(".close-button");
var submitBtn = document.querySelector(".submit-btn");
var resultModal = document.getElementById("resultModal");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

closeButton.addEventListener("click", function () {
    toggleModal();
    // Reset the modal content when closing
    document.getElementById("result").innerText = "";
});

window.addEventListener("click", windowOnClick);

document.getElementById("imageInput").addEventListener("change", function () {
    var input = this;
    if (input.value.length > 0) {
        var fileReader = new FileReader();
        fileReader.onload = function (data) {
            document.querySelector(".image-preview").src = data.target.result;
        };
        fileReader.readAsDataURL(input.files[0]);
        console.log(input.files[0]);
        document.querySelector(".image-preview").style.display = "block";
        document.querySelector(".image-button").innerText = "Choose Different Image";
        document.querySelector(".image-label").innerText = input.files[0].name;
        document.querySelector(".submit-btn").style.display = "block";
        document.querySelector(".right-column").style.display = "block";
    }
});

submitBtn.addEventListener("click", function () {
    console.log("submit");

    // You can replace the following line with the actual result value
    var resultValue = "Your Result Here";
    
    document.getElementById("result").innerText = resultValue;
    
    toggleModal();
    resultModal.style.display = "block";
});

// Close the result modal when clicking outside the modal content
window.addEventListener("click", function (event) {
    if (event.target === resultModal) {
        resultModal.style.display = "none";
    }
});
