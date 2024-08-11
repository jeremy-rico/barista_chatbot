document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send-btn');
    const userMessageInput = document.getElementById('user-message');
    const chatHistory = document.getElementById('chat-history');
    const chatBox = document.getElementById('chat-box')

    // Send message on button click
    sendBtn.addEventListener('click', () => {
        sendMessage();
    });

    // Send message on enter key
    userMessageInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // Start conversation with default message
    default_message = "Hello! How can I assist you with your coffee today?"
    addMessageToChat(default_message, 'bot-message')

    function sendMessage() {
        const userMessage = userMessageInput.value.trim();
        if (userMessage === '') return;

        addMessageToChat(userMessage, 'user-message');
        userMessageInput.value = '';

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            addMessageToChat(data.reply, 'bot-message');
        })
        .catch(error => {
            console.error('Error:', error);
            addMessageToChat('Sorry, something went wrong.', 'bot-message');
        });
    }

    function addMessageToChat(message, messageClass) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', messageClass);
        //messageElement.textContent = message;
	messageElement.innerHTML = marked.parse(message); // Render markdown
        chatHistory.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
