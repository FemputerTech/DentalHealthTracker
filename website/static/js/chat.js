class Chat {
  constructor(messages) {
    this.messageDisplay = document.querySelector(".message-display");
    this.messages = messages;
    this.init();
  }

  init() {
    this.appendMessages();
    const sendButton = document.querySelector(".send");
    sendButton.addEventListener("click", () => this.sendMessage());

    const deleteButton = document.querySelector(".delete");
    deleteButton.addEventListener("click", () => {
      this.deleteMessages();
    });
  }

  appendMessages() {
    this.messages.forEach((message) => {
      if (message.role === "user") {
        const userMessage = document.createElement("div");
        userMessage.classList.add("user-message");
        userMessage.textContent = `You: ${message.content}`;
        this.messageDisplay.appendChild(userMessage);
      } else {
        const botMessage = document.createElement("div");
        botMessage.classList.add("bot-message");
        botMessage.textContent = `Bot: ${message.content}`;
        this.messageDisplay.appendChild(botMessage);
      }
    });
  }

  async sendMessage() {
    const userMessage = document.getElementById("message");
    this.messages.push({ content: userMessage.value, role: "user" });
    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessage.value }),
      });
      const data = await response.json();
      this.messages.push({ content: data.response, role: "bot" });
      this.appendMessages();
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      userMessage.value = "";
    }
  }

  async deleteMessages() {
    fetch("/chat", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    this.messageDisplay.innerHTML = "";
    this.messages = null;
  }
}
