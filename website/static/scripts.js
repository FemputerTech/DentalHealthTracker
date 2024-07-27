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

async function loadAiAssistant() {
  const chatView = document.querySelector(".chat-view");
  const sidebar = document.querySelector(".sidebar");
  const mainDashboardContent = document.querySelector(".main-content");

  chatView.style.display = "flex";

  // Make the sidebar and main content non-interactive
  sidebar.style.pointerEvents = "none";
  mainDashboardContent.style.pointerEvents = "none";
  sidebar.style.opacity = "0.5";
  mainDashboardContent.style.opacity = "0.5";

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
  sidebar.style.pointerEvents = "auto";
  mainDashboardContent.style.pointerEvents = "auto";
  sidebar.style.opacity = "1";
  mainDashboardContent.style.opacity = "1";

  // Save state to localStorage
  localStorage.setItem("chatOpen", "false");
}

async function fetchMessages() {
  const messageDisplay = document.querySelector(".message-display");
  messageDisplay.innerHTML = "";

  try {
    const response = await fetch("/chat", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    const messages = data.messages;

    messages.forEach((message) => {
      console.log("message:", message.role);
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
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}

async function sendMessage() {
  const messageInput = document.getElementById("message");
  const messageDisplay = document.querySelector(".message-display");
  const userMessage = document.createElement("div");
  userMessage.classList.add("user-message");
  userMessage.textContent = `You: ${messageInput.value}`;
  messageDisplay.appendChild(userMessage);

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: messageInput.value }),
    });

    const data = await response.json();
    const botMessage = document.createElement("div");
    botMessage.classList.add("bot-message");
    botMessage.textContent = `Bot: ${data.response}`;
    messageDisplay.appendChild(botMessage);
  } catch (error) {
    console.error("Error sending message:", error);
  } finally {
    messageInput.value = "";
  }
}
