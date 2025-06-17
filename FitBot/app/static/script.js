document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('sendBtn');
    const msgInput = document.getElementById('msg');
    const chatbox = document.getElementById('chatbox');

    sendBtn.addEventListener('click', sendMessage);
    msgInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') sendMessage();
    });

    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.textContent = text;
        message.classList.add('chat-message', sender);
        chatbox.appendChild(message);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function sendMessage() {
        const message = msgInput.value.trim();
        if (message === "") return;

        addMessage(message, 'user');

        fetch('/get_response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, 'bot');
        })
        .catch(err => {
            console.error('Fetch error!', err);
            addMessage("Oops! Something went wrong.", 'bot');
        });

        msgInput.value = "";
    }
});
