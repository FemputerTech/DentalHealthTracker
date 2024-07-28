class ContentManager {
  constructor() {
    this.currentSectionHandler = null;
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

        this.initializeSectionContentHandler(section);
      })
      .catch((error) => console.error("Error loading content:", error));
  }

  async initializeSectionContentHandler(section) {
    switch (section) {
      case "overview":
        this.currentSectionHandler = new ToDo();
      default:
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const contentManager = new ContentManager();
  const savedDashboardSection =
    localStorage.getItem("currentDashboardSection") || "overview";
  contentManager.loadContent(savedDashboardSection);
});
