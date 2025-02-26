// Run this script only after the page fully loads
document.addEventListener("DOMContentLoaded", function () {
  // Select form input fields by their Ids
  let dateInput = document.getElementById("date"); // Date field
  let dateDisplay = document.getElementById("date-display"); // Display selected date in readable format
  let dateError = document.getElementById("date-error"); // error message for invalid daytes
  let timeInput = document.getElementById("time"); // Time field
  let tableInput = document.getElementById("table_number"); // Table # field
  let guestsInput = document.getElementById("guests"); // Guests # field

  // ==========================================
  //Restrict Date Selection to Today or Future
  // ==========================================

  let today = new Date(); // get todays date
  let year = today.getFullYear(); // extract current year
  let month = (today.getMonth() + 1).toString().padStart(2, "0"); // extract current month
  let day = today.getDate().toString().padStart(2, "0"); // extract current day

  let minDate = "${year}-${month}-${day}"; // YYYY-MM-DD format
  dateInput.setAttribute("min", minDate); // set the minimum selectable date in the input field

  // ** Format date to "Month Day, Year" when user selects a date **
  dateInput.addEventListener("change", function () {
    let selectedDate = new Date(this.value); // get the date selected by the user

    // ** Check if selected date is in the past **
    if (selectedDate < today) {
      dateError.textContent = "You cannot select a past date!";
      dateInput.value = ""; //Reset invalid input
    } else {
      dateError.textContent = ""; // Clear error
      dateDisplay.textContent = selectedDate.toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      }); // display date in month day, year format
    }
  });

  // ====================================================
  // ** Restrict Time Selection between 9 AM - 9 PM **
  // ====================================================

  timeInput.addEventListener("input", function () {
    let time = timeInput.value; // Get user-selected time

    // if time is before 9AM or after 9 pm, show an alert and reset the input
    if (time < "09:00" || time > "21:00") {
      alert("Please select a time between 9 am and 9 pm.");
      timeInput.value = ""; // Reset invalid input
    }
  });

  // =====================================================
  //Restrict Table Number Selection (1-20) **
  // =====================================================

  tableInput.addEventListener("input", function () {
    let tableNumber = parseInt(tableInput.value, 10); // Convert input value to a number

    if (tableNumber < 1) {
      tableInput.value = 1; // if number is below 1 reset to 1
    } else if (tableNumber > 20) {
      tableInput.value = 20; // if number is more than 20 reset to 20
    }
  });

  // =========================================================
  // Restrict Guest Selection (1-10) per table
  // =========================================================

  guestsInput.addEventListener("input", function () {
    let guests = parseInt(guestsInput.value, 10); // Convert input value to a number

    if (guests < 1) {
      guestsInput.value = 1; // if guest are below 1 reset to 1
    } else if (guests > 10) {
      guestsInput.value = 10; // if guests are more than 10 reset to 10
    }
  });
});
