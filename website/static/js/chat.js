class Chat {
  constructor(messages) {
    this.messageDisplay = document.querySelector(".message-display");
    this.messages = messages;
    this.init();
  }

  init() {
    this.messages.forEach((message) => {
      this.appendMessage(message);
    });
    const sendButton = document.querySelector(".send");
    sendButton.addEventListener("click", () => this.sendMessage());

    const deleteButton = document.querySelector(".delete");
    deleteButton.addEventListener("click", () => {
      this.deleteMessages();
    });
  }

  appendMessage(message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList = "message-container";
    this.messageDisplay.appendChild(messageDiv);
    if (message.role === "user") {
      const userMessage = document.createElement("p");
      userMessage.classList.add("user-message");
      userMessage.textContent = `${message.content}`;
      messageDiv.appendChild(userMessage);
    } else {
      const botMessage = document.createElement("p");
      botMessage.classList.add("bot-message");
      botMessage.textContent = `${message.content}`;
      messageDiv.appendChild(botMessage);
    }
  }

  async sendMessage() {
    const userMessageInput = document.getElementById("message");
    const userMessageContent = userMessageInput.value;
    const userMessage = { content: userMessageContent, role: "user" };
    this.appendMessage(userMessage);
    userMessageInput.value = "";
    this.messages.push(userMessage);
    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessageContent }),
      });
      const data = await response.json();

      const botMessage = { content: data.response, role: "bot" };
      this.appendMessage(botMessage);
      this.messages.push(botMessage);
    } catch (error) {
      console.error("Error sending message:", error);
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
    this.messages = [];
  }
}
