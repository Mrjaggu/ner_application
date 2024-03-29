document.addEventListener("DOMContentLoaded", function() {
    // Attach the form submit handler
    const chatForm = document.getElementById('chat-form');
    const chatBody = document.getElementById('chat-body');
    const userInput = chatForm.querySelector('input[name="user_input"]');

    chatForm.onsubmit = function(e) {
        e.preventDefault();

        const message = userInput.value.trim();
        if (message) {
            // Append message to chat body as user message
            appendMessage(message, 'user');

            // Send the message to Flask server
            fetch('/ask', {
                method: 'POST',
                body: JSON.stringify({ user_input: message }), // Make sure this key is 'user_input'
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                // Append the response to chat body as bot message
                appendMessage(data.response, 'bot');
            })
            .catch(error => {
                console.error('Error:', error);
            });

            // Clear input after sending
            userInput.value = '';
        }
    };

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        const messageText = document.createElement('p');
        messageText.textContent = text;

        const timestampSpan = document.createElement('span');
        timestampSpan.classList.add('timestamp');
        // Set the current timestamp or format as you wish
        timestampSpan.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        messageDiv.appendChild(messageText);
        messageDiv.appendChild(timestampSpan);
        chatBody.appendChild(messageDiv);

        // Scroll to the bottom of the chat body to show new message
        chatBody.scrollTop = chatBody.scrollHeight;
    }
     // Post a default bot message as soon as the page loads
     appendMessage('Hi! I am your NLP buddy. How can I help you?', 'bot');

});
