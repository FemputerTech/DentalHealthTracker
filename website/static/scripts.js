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

  if (boxIcon.getAttribute("name") === "chevrons-right") {
    boxIcon.setAttribute("name", "chevrons-left");
    sidebar.classList.add("expanded");
    dashboard.classList.add("expanded");
  } else {
    boxIcon.setAttribute("name", "chevrons-right");
    sidebar.classList.remove("expanded");
    dashboard.classList.remove("expanded");
  }

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
