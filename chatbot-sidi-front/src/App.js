import React, { useState, useLayoutEffect, useRef } from 'react';
import axios from 'axios';
import Logo from './images/Logo.png';
import Send from './images/send.png';
import ProfileImage from './images/profile.png';
import Chat from './images/Chat.png'
import './App.css';


function Chatbot() {
  const [userInput, setUserInput] = useState('');
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: (
        <React.Fragment>
          Olá, seja bem-vindo ao Chatbot SiDi 👋😊. O que você quer fazer? Digite "<span className='bold'>!menu</span>" para saber as opções.
        </React.Fragment>
      ),
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

  useLayoutEffect(() => {
    if (botResponse) {
      const regex = /(https?:\/\/[^\s]+)/g;
      const parts = botResponse.split("\n");
  
      const formattedResponse = parts.map((part, index) => {
        const commandsRegex = /(!\w+|:\s*$)/g;
        const matches = part.match(commandsRegex);
  
        if (matches) {
          const commandElements = part.split(commandsRegex).map((element, elementIndex) => {
            if (element.match(commandsRegex)) {
              return <span className='bold' key={elementIndex}>{element}</span>;
            } else {
              return element;
            }
          });
  
          return (
            <div key={index}>
              {commandElements}
            </div>
          );
        } else if (part.match(regex)) {
          const link = part.match(regex)[0];
          const text = part.replace(link, '');
  
          return (
            <div key={index}>
              <span className='bold'>{text}</span>
              <a href={link} target="_blank" rel="noopener noreferrer">
                clique aqui!
              </a>
            </div>
          );
        } else {
          return <div key={index}>{part}</div>;
        }
      });


      setMessages(prevMessages => [
        ...prevMessages,
        {
          id: prevMessages.length + 2,
          text: formattedResponse,
          sender: 'bot',
        }
      ]);
    }
  }, [botResponse]);

  useLayoutEffect(() => {
    const style = document.createElement('style');
    style.innerHTML = `
      ::-webkit-scrollbar {
        width: 8px; /* Largura da barra de rolagem */
      }
      
      ::-webkit-scrollbar-track {
        background-color: #FEFEFE; /* Cor de fundo da barra de rolagem */
      }
      
      ::-webkit-scrollbar-thumb {
        background-color: #b75eff; /* Cor do "polegar" da barra de rolagem */
      }
    `;
    document.head.appendChild(style);
  
    messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);
  

  return (
    <div className="chat-container">
      <div className="chat-image">
        <div className="logo-container">
          <img src={Chat} alt="logo" />
          <h1 className="chat-title">ChatBot</h1>
        </div>
      </div>

      {messages.map((message) => (
        <div
          key={message.id}
          className={`message-container ${message.sender}-message`}
        >
          <img src={message.sender === 'user' ? message.image : Chat} alt="Chatbot Avatar" />
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

function App() {
  return (
    <div className="App">
      <div className="logo-container">
        <img src={Logo} alt="Logo" className="logo" />
      </div>
      <Chatbot />
    </div>
  );
}

export default App;

