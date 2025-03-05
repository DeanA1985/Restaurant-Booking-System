// Run this script only after the page fully loads
document.addEventListener("DOMContentLoaded", function () {
  let bookingForm = document.getElementById("bookingForm");
  let submitButton = document.querySelector("button[type='submit']");

  function checkFormValidity() {
    let table = document.getElementById("table_number").value.trim();
    let date = document.getElementById("date").value.trim();
    let time = document.getElementById("time").value.trim();
    let guests = document.getElementById("guests").value.trim();

    submitButton.disabled = !table || !date || !time || !guests;
  }

  // Check form validity on every input change
  document.querySelectorAll("#bookingForm input").forEach((input) => {
    input.addEventListener("input", checkFormValidity);
  });

  // Prevent form submission if fields are empty
  bookingForm.addEventListener("submit", function (event) {
    if (submitButton.disabled) {
      event.preventDefault();
      alert("All fields must be filled before submitting!");
    }
  });

  checkFormValidity(); // Initial check on page load
});

// ==========================================
//Restrict Date Selection to Today or Future
// ==========================================

let dateInput = document.getElementById("date");
let today = new Date();
let year = today.getFullYear();
let month = (today.getMonth() + 1).toString().padStart(2, "0");
let day = today.getDate().toString().padStart(2, "0");
let minDate = "${year}-${month}-${day}";
dateInput.setAttribute("min", minDate);

// Prevent selecting a past date manually
dateInput.addEventListener("change", function () {
  let selectedDate = new Date(dateInput.value);
  if (selectedDate < today) {
    alert("Booking date cannot be in the past.");
    dateInput.value = ""; //Reset invalid input
  }
});

// =====================================================
//Restrict Table Number Selection (1-20) **
// =====================================================
let tableInput = document.getElementById("table_number");
tableInput.addEventListener("input", function () {
  let tableNumber = parseInt(tableInput.value, 10);
  if (tableNumber < 1) {
    tableInput.value = 1;
  } else if (tableNumber > 20) {
    tableInput.value = 20;
  }
});

// =========================================================
// Restrict Guest Selection (1-10) per table
// =========================================================
let guestsInput = document.getElementById("guests");
guestsInput.addEventListener("input", function () {
  let guests = parseInt(guestsInput.value, 10);
  if (guests < 1) {
    guestsInput.value = 1;
  } else if (guests > 10) {
    guestsInput.value = 10;
  }
});
