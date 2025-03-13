/**
 * Runs the script after the DOM has fully loaded.
 * Initialises form and submit button references,
 * and sets up valiadtion logic.
 */
document.addEventListener("DOMContentLoaded", function () {
  let bookingForm = document.getElementById("bookingForm");
  let submitButton = document.querySelector("button[type='submit']");

/**
 * Checks whether all form fields have valid input.
 * Disables the submit button if any field is empty.
 */  

  function checkFormValidity() {
    let table = document.getElementById("table_number").value.trim();
    let date = document.getElementById("date").value.trim();
    let time = document.getElementById("time").value.trim();
    let guests = document.getElementById("guests").value.trim();

    submitButton.disabled = !table || !date || !time || !guests;
  }

/**
 * Adds input event listener to  form fields.
 * Revalidates from fields on user input.
 */
  document.querySelectorAll("#bookingForm input").forEach((input) => {
    input.addEventListener("input", checkFormValidity);
  });

/**
 * Prevents form submission if submit button is disabled.
 * Alerts user that all fields must be filled.
 */
  bookingForm.addEventListener("submit", function (event) {
    if (submitButton.disabled) {
      event.preventDefault();
      alert("All fields must be filled before submitting!");
    }
  });
  // Initial validation check on page load
  checkFormValidity(); 
});

/**
 * Restricts date input to future dates only.
 * Sets the minimum date to tomorrow.
 */
let dateInput = document.getElementById("date");
let today = new Date();
today.setHours(0, 0, 0, 0); // Normalise time to 00:00:00

// Set min date to tomorrow
let tomorrow = new Date(today);
tomorrow.setDate(tomorrow.getDate() + 1);

// Format as yyyy-mm-dd for HTML input
let year = tomorrow.getFullYear();
let month = (tomorrow.getMonth() + 1).toString().padStart(2, "0");
let day = tomorrow.getDate().toString().padStart(2, "0");
let minDate = "${year}-${month}-${day}";
dateInput.setAttribute("min", minDate);

/**
 * Prevents the user from manually selecting today's date or
 * past dates. Alerts user and resets the input if invalid.
 */
dateInput.addEventListener("change", function () {
  let selectedDate = new Date(dateInput.value);
  selectedDate.setHours(0, 0, 0, 0);

  if (selectedDate < tomorrow) {
    alert("Bookings must be made at least one day in advance.");
    dateInput.value = ""; //Reset invalid input
  }
});

/**
 * Ensures table number is between 1 and 20.
 * Adjusts value automatically if outside this range.
 */
let tableInput = document.getElementById("table_number");
tableInput.addEventListener("input", function () {
  let tableNumber = parseInt(tableInput.value, 10);
  if (tableNumber < 1) {
    tableInput.value = 1;
  } else if (tableNumber > 20) {
    tableInput.value = 20;
  }
});

/**
 * Ensures the number of guests is between 1 and 10.
 * Adjusts value automatically if outside this range.
 */
let guestsInput = document.getElementById("guests");
guestsInput.addEventListener("input", function () {
  let guests = parseInt(guestsInput.value, 10);
  if (guests < 1) {
    guestsInput.value = 1;
  } else if (guests > 10) {
    guestsInput.value = 10;
  }
});
