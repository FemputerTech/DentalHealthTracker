function toggleNavList() {
  const navList = document.querySelector(".nav-list");

  if (navList.style.display === "") {
    navList.style.display = "flex";
  } else {
    navList.style.display = "";
  }
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
    return data.messages;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}
