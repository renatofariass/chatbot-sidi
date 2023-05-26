import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Logo from './Logo.png';
import Bot from './bot.jpeg';
import Send from './send.png';
import ProfileImage from './profile.png';
import './App.css';

function Chatbot() {
  const [userInput, setUserInput] = useState('');
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: 'Olá, seja bem-vindo ao Chatbot SiDi. O que você quer fazer? Digite "!menu" para saber as opções.',
      sender: 'bot',
    },
  ]);
  const [botResponse, setBotResponse] = useState('');
  const [buttonHovered, setButtonHovered] = useState(false);
  const messagesEndRef = useRef(null);

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSendMessage = () => {
    if (userInput.trim() !== '') {
      const newUserMessage = {
        id: messages.length + 1,
        text: userInput,
        sender: 'user',
        image: ProfileImage,
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

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      handleSendMessage();
    }
  };

  const handleButtonMouseEnter = () => {
    setButtonHovered(true);
  };

  const handleButtonMouseLeave = () => {
    setButtonHovered(false);
  };

  useEffect(() => {
    if (botResponse) {
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

  useEffect(() => {
    messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="chat-container">
      <div className="chat-image">
        <img src={Logo} alt="logo" />
      </div>

      {messages.map((message) => (
        <div
          key={message.id}
          className={`message-container ${message.sender}-message`}
        >
          <img src={message.sender === 'user' ? message.image : Bot} alt="Chatbot Avatar" />
          <p>{message.text}</p>
        </div>
      ))}

      <div ref={messagesEndRef} />

      <div className="user-input-container">
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          placeholder="Digite sua mensagem"
        />
        <img
          src={Send}
          alt="Enviar"
          onClick={handleSendMessage}
          onMouseEnter={handleButtonMouseEnter}
          onMouseLeave={handleButtonMouseLeave}
          style={{
            marginLeft: '0.7%',
            filter: buttonHovered ? 'brightness(70%)' : 'none',
            cursor: 'pointer',
          }}
        />
      </div>
    </div>
  );
}

export default Chatbot;