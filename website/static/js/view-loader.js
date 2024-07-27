class ViewLoader {
  constructor() {
    this.sidebarLinks = document.querySelectorAll(".sidebar .nav-link.view");
    this.popupView = document.querySelector(".popup-view");
    this.closeButton = null;
    this.init();
  }

  init() {
    this.sidebarLinks.forEach((link) => {
      link.addEventListener("click", () => {
        const view = link.getAttribute("data-section");
        this.loadView(view);
      });
    });

    const storedView = localStorage.getItem("currentPopupView");
    if (storedView) {
      this.loadView(storedView);
    }
  }

  async loadView(view) {
    this.popupView.style.display = "flex";
    fetch(`/dashboard/view/${view}`)
      .then((response) => response.text())
      .then((html) => {
        this.popupView.innerHTML = html;
        this.closeButton = this.popupView.querySelector(".close");
        if (this.closeButton) {
          this.closeButton.addEventListener("click", () => {
            this.closeView();
          });
        }
        this.toggle_main_interaction("0.5", "none");
        localStorage.setItem("currentPopupView", view);
      })
      .catch((error) => console.error("Error loading content:", error));
  }

  closeView() {
    this.popupView.style.display = "";
    this.toggle_main_interaction("1", "auto");
    localStorage.removeItem("currentPopupView");
    this.closeButton = null;
  }

  toggle_main_interaction(opacity, pointerEvents) {
    const sidebar = document.querySelector(".sidebar");
    const dashboard = document.querySelector("main");

    sidebar.style.pointerEvents = pointerEvents;
    dashboard.style.pointerEvents = pointerEvents;
    sidebar.style.opacity = opacity;
    dashboard.style.opacity = opacity;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  new ViewLoader();
});
