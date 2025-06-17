function toggleChatbot() {
  const chatbot = document.getElementById('chatbotWindow');
  chatbot.style.display = chatbot.style.display === 'flex' ? 'none' : 'flex';
}

function sendMessage(event) {
  if (event.key === 'Enter') {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    if (message === "") return;

    const chatBody = document.getElementById('chatMessages');
    chatBody.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    input.value = "";

    // Simulated bot reply
    setTimeout(() => {
      chatBody.innerHTML += `<p><strong>Bot:</strong> Thanks for your message!</p>`;
      chatBody.scrollTop = chatBody.scrollHeight;
    }, 500);
  }
}