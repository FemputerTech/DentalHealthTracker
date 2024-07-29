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
  }
}

function closePopup(popup) {
  const popupContainer = document.getElementById(popup);
  popupContainer.style.display = "none";
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

async function fetchMessages() {
  const messageDisplay = document.querySelector(".message-display");
  messageDisplay.innerHTML = "";
  try {
    const response = await fetch("/chat", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data.messages;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const dateContainer = document.querySelector(".date-container");
  const today = new Date();
  const options = { year: "numeric", month: "long", day: "numeric" };
  const formattedDate = today.toLocaleDateString(undefined, options);
  dateContainer.textContent = `Today's Date: ${formattedDate}`;
});
