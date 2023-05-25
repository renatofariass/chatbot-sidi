import logo from './Logo.png';
import bot from './bot.jpeg';
import send from './send.png';
import profileImage from './profile.png';
import './App.css'
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Chatbot() {
  const [userInput, setUserInput] = useState('');
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: 'Olá, seja bem vindo ao Chatbot SiDi. O que você quer fazer? Digite "!menu" para saber as opções.',
      sender: 'bot',
    },
  ]);
  const [botResponse, setBotResponse] = useState('');

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSendMessage = () => {
    if (userInput.trim() !== '') {
      const newUserMessage = {
        id: messages.length + 1,
        text: userInput,
        sender: 'user',
        image: profileImage,
      };

      setMessages([...messages, newUserMessage]);
      setUserInput('');

      axios
        .post('http://127.0.0.1:5002/chatbot', { resposta: userInput }, { headers: { 'Content-Type': 'application/json' } })
        .then(response => {
          setBotResponse(response.data.chatbot);
        })
        .catch(error => {
          console.error('Erro ao enviar a mensagem para o chatbot:', error);
        });
    }
  };

  useEffect(() => {
    if (botResponse !== '') {
      setMessages(prevMessages => [
        ...prevMessages,
        {
          id: prevMessages.length + 2,
          text: `${botResponse}`,
          sender: 'bot',
        }
      ]);
    }
  }, [botResponse]);

  return (
    <body>
      <div className="chat-container">
        <div className="chat-image">
          <img src={logo} alt="logo" />
        </div>

        {messages.map((message) => (
          <div
            key={message.id}
            className={`message-container ${message.sender}-message`}
          >
            <img src={message.sender === 'user' ? message.image : bot} alt="Chatbot Avatar" />
            <p>{message.text}</p>
          </div>
        ))}

        <div className="user-input-container">
          <input
            type="text"
            value={userInput}
            onChange={handleInputChange}
            placeholder="Digite sua mensagem"
          />
          <img
            src={send}
            alt="Enviar"
            onClick={handleSendMessage}
            style={{ marginLeft: '0.7%' }}
          />
        </div>
      </div>
    </body>
  );
}

export default Chatbot;
