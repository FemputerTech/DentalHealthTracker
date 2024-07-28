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

async function fetchAccount() {
  try {
    const response = await fetch("/account", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    console.log("user:", data.user);
    return data.messages;
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const dateContainer = document.querySelector(".date-container");
  const today = new Date();
  const options = { year: "numeric", month: "long", day: "numeric" };
  const formattedDate = today.toLocaleDateString(undefined, options);
  dateContainer.textContent = `Today's Date: ${formattedDate}`;
});
