class ContentManager {
  constructor() {
    this.loadContentButtons = document.querySelectorAll(".label-button");
    this.sidebarLinks = document.querySelectorAll(".sidebar .nav-link.content");
    this.init();
  }

  init() {
    this.loadContentButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const section = button.getAttribute("data-section");
        this.loadContent(section);
      });
    });
    this.sidebarLinks.forEach((link) => {
      link.addEventListener("click", () => {
        const section = link.getAttribute("data-section");
        this.loadContent(section);
      });
    });
  }

  async loadContent(section) {
    fetch(`/dashboard/${section}`)
      .then((response) => response.text())
      .then((html) => {
        document.querySelector(".dashboard-content").innerHTML = html;
        localStorage.setItem("currentDashboardSection", section);
      })
      .catch((error) => console.error("Error loading content:", error));
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const contentManager = new ContentManager();
  const savedDashboardSection =
    localStorage.getItem("currentDashboardSection") || "overview";
  contentManager.loadContent(savedDashboardSection);
});
