function toggleNavList() {
  const navList = document.querySelector(".nav-list");

  if (navList.style.display === "") {
    navList.style.display = "flex";
  } else {
    navList.style.display = "";
  }
}

function displayPopup(popup) {
  document.querySelectorAll(".popup-container").forEach((view) => {
    view.style.display = "none";
  });

  const popupContainer = document.getElementById(popup);
  if (popupContainer) {
    popupContainer.style.display = "flex";
    toggle_main_interaction("0.5", "none", "rgba(0, 0, 0, 0.2)");
  }
}

function toggle_main_interaction(opacity, pointerEvents, color) {
  const sidebar = document.querySelector(".sidebar");
  const dashboard = document.querySelector("main");

  sidebar.style.pointerEvents = pointerEvents;
  sidebar.style.opacity = opacity;

  dashboard.style.pointerEvents = pointerEvents;
  dashboard.style.opacity = opacity;
  dashboard.style.backgroundColor = color;
}

function closePopup(popup) {
  const popupContainer = document.getElementById(popup);
  popupContainer.style.display = "none";
  toggle_main_interaction("1", "auto", "transparent");
}

function displayDashboard(label) {
  document.querySelectorAll(".dashboard-content").forEach((section) => {
    section.style.display = "none";
  });

  const dashboardContent = document.getElementById(label);
  if (dashboardContent) {
    dashboardContent.style.display = "block";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  displayDashboard("overview");
});

document.addEventListener("DOMContentLoaded", function () {
  const dateContainer = document.querySelector(".date-container");
  const today = new Date();
  const options = { year: "numeric", month: "long", day: "numeric" };
  const formattedDate = today.toLocaleDateString(undefined, options);
  dateContainer.textContent = `Today's Date: ${formattedDate}`;
});

function editUserInfo(fieldId) {
  const field = document.getElementById(fieldId);
  field.removeAttribute("readonly");
  field.focus();
}
