import React, { useState } from 'react';
import { ChakraProvider } from '@chakra-ui/react';
import WelcomePage from './WelcomePage'; 
import WelcomeScreen from "./components/ui/WelcomeScreen.jsx";

function App() {
  const [name, setName] = useState(null);

  const onNext = (userName) => {
    setName(userName);
    console.log(userName);
  };

  return (
    <ChakraProvider>
      {!name ? (
        <WelcomePage onProceed={onNext} />
      ) : (
        <WelcomeScreen onNext={onNext} />
      )}
    </ChakraProvider>
  );
}

export default App;

