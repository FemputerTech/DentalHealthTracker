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
  const header = document.querySelector(".header-authenticated");
  const sidebar = document.querySelector(".sidebar");

  if (boxIcon.getAttribute("name") === "chevrons-right") {
    boxIcon.setAttribute("name", "chevrons-left");
    sidebar.classList.add("expanded");
    header.classList.add("expanded");
  } else {
    boxIcon.setAttribute("name", "chevrons-right");
    sidebar.classList.remove("expanded");
    header.classList.remove("expanded");
  }

  navLabels.forEach((navLabel) => {
    if (navLabel.style.display === "") {
      navLabel.style.display = "flex";
    } else {
      navLabel.style.display = "";
    }
  });
}
