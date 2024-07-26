function toggleNavList() {
  const navList = document.querySelector(".nav-list");

  if (navList.style.display === "") {
    navList.style.display = "flex";
  } else {
    navList.style.display = "";
  }
}

function toggleSidebar() {
  const sidebarToggle = document.querySelector(".sidebar-toggle");
  const boxIcon = sidebarToggle.querySelector("box-icon");
  const navLabels = document.querySelectorAll(".nav-label");
  const sidebar = document.querySelector(".sidebar");
  const dashboard = document.querySelector(".main-dashboard");

  let isExpanded = boxIcon.getAttribute("name") === "chevrons-left";

  if (isExpanded) {
    boxIcon.setAttribute("name", "chevrons-right");
    sidebar.classList.remove("expanded");
    dashboard.classList.remove("expanded");
  } else {
    boxIcon.setAttribute("name", "chevrons-left");
    sidebar.classList.add("expanded");
    dashboard.classList.add("expanded");
  }

  localStorage.setItem("sidebarExpanded", !isExpanded);

  navLabels.forEach((navLabel) => {
    if (navLabel.style.display === "") {
      navLabel.style.display = "flex";
    } else {
      navLabel.style.display = "";
    }
  });
}

function loadContent(section) {
  fetch(`/dashboard/${section}`)
    .then((response) => response.text())
    .then((html) => {
      document.querySelector(".dashboard-content").innerHTML = html;
      localStorage.setItem("currentDashboardSection", section);
    })
    .catch((error) => console.error("Error loading content:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  const savedDashboardSection =
    localStorage.getItem("currentDashboardSection") || "overview";
  loadContent(savedDashboardSection);
});

function loadAiAssistant() {
  const chatView = document.querySelector(".chat-view");
  const sidebar = document.querySelector(".sidebar");
  const mainDashboardContent = document.querySelector(".main-content");

  chatView.style.display = "flex";

  // Make the sidebar and main content non-interactive
  sidebar.style.pointerEvents = "none";
  mainDashboardContent.style.pointerEvents = "none";
  sidebar.style.opacity = "0.7";
  mainDashboardContent.style.opacity = "0.7";

  fetch("/dashboard/ai-assistant")
    .then((response) => response.text())
    .then((html) => {
      chatView.innerHTML = html;
    })
    .catch((error) => console.error("Error loading content:", error));
}

function closeAiAssistant() {
  const chatView = document.querySelector(".chat-view");
  const sidebar = document.querySelector(".sidebar");
  const mainDashboardContent = document.querySelector(".main-content");
  chatView.style.display = "";

  // Re-enable the sidebar and main content
  sidebar.style.pointerEvents = "auto";
  mainDashboardContent.style.pointerEvents = "auto";
  sidebar.style.opacity = "1";
  mainDashboardContent.style.opacity = "1";
}
