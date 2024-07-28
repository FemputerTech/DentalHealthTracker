class PopupManager {
  constructor() {
    this.currentPopupHandler = null;
    this.sidebarLinks = document.querySelectorAll(".sidebar .nav-link.view");
    this.popupContainer = document.querySelector(".popup-container");
    this.init();
  }

  init() {
    this.sidebarLinks.forEach((link) => {
      link.addEventListener("click", () => {
        const popup = link.getAttribute("data-popup");
        this.loadPopup(popup);
      });
    });
    // const storedView = localStorage.getItem("currentPopupView");
    // if (storedView) {
    // this.loadPopup(storedView);
    // }
  }

  async loadPopup(popup) {
    this.popupContainer.style.display = "flex";
    fetch(`/popup/${popup}`)
      .then((response) => response.text())
      .then((html) => {
        this.popupContainer.innerHTML = html;
        const closeButton = this.popupContainer.querySelector(
          ".popup-close-button"
        );
        if (closeButton) {
          closeButton.addEventListener("click", () => {
            this.closePopup();
          });
        }
        this.toggle_main_interaction("0.5", "none", "rgba(0, 0, 0, 0.2)");
        // localStorage.setItem("currentPopupView", popup);

        this.initializePopupContentHandler(popup);
      })
      .catch((error) => console.error("Error loading content:", error));
  }

  async initializePopupContentHandler(popup) {
    switch (popup) {
      case "chat":
        const messages = await fetchMessages();
        this.currentPopupHandler = new Chat(messages);
      default:
    }
  }

  closePopup() {
    this.popupContainer.style.display = "";
    this.toggle_main_interaction("1", "auto", "transparent");
    localStorage.removeItem("currentPopupView");
    this.closeButton = null;
  }

  toggle_main_interaction(opacity, pointerEvents, color) {
    const sidebar = document.querySelector(".sidebar");
    const dashboard = document.querySelector("main");

    sidebar.style.pointerEvents = pointerEvents;
    sidebar.style.opacity = opacity;

    dashboard.style.pointerEvents = pointerEvents;
    dashboard.style.opacity = opacity;
    dashboard.style.backgroundColor = color;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  new PopupManager();
});
