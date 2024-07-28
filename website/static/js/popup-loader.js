class PopupLoader {
  constructor() {
    this.sidebarLinks = document.querySelectorAll(".sidebar .nav-link.view");
    this.popupContainer = document.querySelector(".popup-container");
    this.closeButton = null;
    this.init();
  }

  init() {
    this.sidebarLinks.forEach((link) => {
      link.addEventListener("click", () => {
        const popup = link.getAttribute("data-popup");
        this.loadPopup(popup);
      });
    });
    const storedView = localStorage.getItem("currentPopupView");
    if (storedView) {
      this.loadPopup(storedView);
    }
  }

  async loadPopup(popup) {
    this.popupContainer.style.display = "flex";
    fetch(`/popup/${popup}`)
      .then((response) => response.text())
      .then((html) => {
        this.popupContainer.innerHTML = html;
        this.closeButton = this.popupContainer.querySelector(".close");
        if (this.closeButton) {
          this.closeButton.addEventListener("click", () => {
            this.closePopup();
          });
        }
        this.toggle_main_interaction("0.5", "none");
        localStorage.setItem("currentPopupView", popup);
      })
      .catch((error) => console.error("Error loading content:", error));
  }

  closePopup() {
    this.popupContainer.style.display = "";
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
  new PopupLoader();
});