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

async function loadContent(section) {
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

function isInteractive(opacity, pointerEvents) {
  sidebar.style.pointerEvents = pointerEvents;
  mainDashboardContent.style.pointerEvents = pointerEventss;
  sidebar.style.opacity = opacity;
  mainDashboardContent.style.opacity = opacity;
}

async function loadAiAssistant() {
  const chatView = document.querySelector(".chat-view");
  const sidebar = document.querySelector(".sidebar");
  const mainDashboardContent = document.querySelector(".main-content");

  chatView.style.display = "flex";

  // Make the sidebar and main content non-interactive
  isInteractive("0.5", "none");

  // Save state to localStorage
  localStorage.setItem("chatOpen", "true");

  fetch("/dashboard/ai-assistant")
    .then((response) => response.text())
    .then((html) => {
      chatView.innerHTML = html;
      fetchMessages();
    })
    .catch((error) => console.error("Error loading content:", error));
}

function closeAiAssistant() {
  const chatView = document.querySelector(".chat-view");
  const sidebar = document.querySelector(".sidebar");
  const mainDashboardContent = document.querySelector(".main-content");
  chatView.style.display = "";

  // Re-enable the sidebar and main content
  isInteractive("1", "auto");

  // Save state to localStorage
  localStorage.setItem("chatOpen", "false");
}

function appendMessages(messages) {
  const messageDisplay = document.querySelector(".message-display");
  messageDisplay.innerHTML = "";

  messages.forEach((message) => {
    if (message.role === "user") {
      const userMessage = document.createElement("div");
      userMessage.classList.add("user-message");
      userMessage.textContent = `You: ${message.content}`;
      messageDisplay.appendChild(userMessage);
    } else {
      const botMessage = document.createElement("div");
      botMessage.classList.add("bot-message");
      botMessage.textContent = `Bot: ${message.content}`;
      messageDisplay.appendChild(botMessage);
    }
  });
}

async function fetchMessages() {
  try {
    const response = await fetch("/chat", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    const messages = data.messages;
    appendMessages(messages);
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}

async function sendMessage() {
  let messages = [];
  const userMessage = document.getElementById("message");
  messages.append({ content: userMessage.value, role: "user" });
  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: messageInput.value }),
    });
    const data = await response.json();
    messages.append({ content: data.response, role: "bot" });
    appendMessages(messages);
  } catch (error) {
    console.error("Error sending message:", error);
  } finally {
    messageInput.value = "";
  }
}
