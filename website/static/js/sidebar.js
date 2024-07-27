class Sidebar {
  constructor() {
    this.toggleButton = document.querySelector(".sidebar-toggle");
    this.boxIcon = this.toggleButton.querySelector("box-icon");
    this.navLabels = document.querySelectorAll(".nav-label");
    this.sidebar = document.querySelector(".sidebar");
    this.dashboard = document.querySelector("main");
    this.init();
  }

  init() {
    this.toggleButton.addEventListener("click", () => this.toggle());
  }

  toggle() {
    const isExpanded = this.boxIcon.getAttribute("name") === "chevrons-left";
    if (isExpanded) {
      this.boxIcon.setAttribute("name", "chevrons-right");
      this.sidebar.classList.remove("expanded");
      this.dashboard.classList.remove("expanded");
    } else {
      this.boxIcon.setAttribute("name", "chevrons-left");
      this.sidebar.classList.add("expanded");
      this.dashboard.classList.add("expanded");
    }

    localStorage.setItem("sidebarExpanded", !isExpanded);

    this.navLabels.forEach((navLabel) => {
      if (navLabel.style.display === "") {
        navLabel.style.display = "flex";
      } else {
        navLabel.style.display = "";
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  new Sidebar();
});
