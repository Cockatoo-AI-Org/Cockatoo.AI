// src/Chat.js 
// Author: Louis Chang
// DESCRIPTION: This file contains the implementation of a chat component.
// Version 0.2 - 2024/06/09

// - Version 0.1 - 2024/06/02: Create the chat component.
// - Version 0.2 - 2024/06/09: Add the additional functionality to send messages to the server and file upload.

import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { FiPaperclip, FiMic } from 'react-icons/fi';

function Chat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [fileName, setFileName] = useState('');

    const sendMessage = async () => {
        if (input.trim() === '') return;

        const newMessage = { role: 'user', content: input };
        setMessages([...messages, newMessage]);

        const response = await fetch('http://localhost:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: input }),
        });
        const data = await response.json();

        setMessages([...messages, newMessage, { role: 'bot', content: data.reply }]);
        setInput('');
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    const handleFileUpload = (event) => {
        const file = event.target.files[0];
        setFileName(file.name);
        // Handle file upload logic here
    };

    const handleVoiceInput = () => {
        // Handle voice input logic here
        alert('Voice input feature is not implemented yet.');
    };

    return (
        <div className="container mt-5">
            <h1 className="text-center mb-4">LLM Chat</h1>
            <div className="card">
                <div className="card-body">
                    <div className="chat-box mb-3" style={{ height: '300px', overflowY: 'scroll' }}>
                        {messages.map((msg, index) => (
                            <div key={index} className={`alert ${msg.role === 'user' ? 'alert-primary' : 'alert-secondary'}`}>
                                <b>{msg.role}:</b> {msg.content}
                            </div>
                        ))}
                    </div>
                    <div className="input-group">
                        <div className="input-group-prepend">
                            <label className="input-group-text" htmlFor="file-upload">
                                <FiPaperclip />
                            </label>
                            <input 
                                type="file"
                                className="form-control d-none"
                                id="file-upload"
                                onChange={handleFileUpload}
                            />
                        </div>
                        {fileName && <span className="input-group-text">{fileName}</span>}
                        <input 
                            type="text"
                            className="form-control"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Type your message..."
                        />
                        <div className="input-group-append">
                            <button className="btn btn-primary" onClick={sendMessage}>Send</button>
                            <button className="btn btn-secondary" onClick={handleVoiceInput}><FiMic /></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Chat;
