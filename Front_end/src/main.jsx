import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import { ChakraProvider } from '@chakra-ui/react';
import WelcomePage from './WelcomePage';
import GamePage from './GamePage'; // You will need to create this component

const App = () => {
  const [playerName, setPlayerName] = useState('');

  return (
    <ChakraProvider>
      {playerName ? (
        <GamePage playerName={playerName} />
      ) : (
        <WelcomePage onProceed={setPlayerName} />
      )}
    </ChakraProvider>
  );
};

ReactDOM.createRoot(document.getElementById('root')).render(<App />);