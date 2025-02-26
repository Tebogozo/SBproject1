import React, { useState } from 'react';
//import WelcomeScreen from "./components/WelcomeScreen.jsx";
import GamePage from './GamePage.jsx';
import WelcomePage from './WelcomePage.jsx';


function App() {
  const [startGame, setStartGame] = useState(false);

  const onNext = () => {
    setStartGame(true);
  };

  return (
      <>
      {!startGame ? (
        <WelcomePage onProceed={onNext} />
      ) : (
        <GamePage onNext={onNext} />
      )}
      </>
      
  );
}

export default App;

