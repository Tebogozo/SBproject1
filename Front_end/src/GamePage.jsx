import React, { useState } from 'react';
import { Box, Text, Button } from '@chakra-ui/react';
import GameScreen from './components/GameScreen.jsx'


// track all questions using index
// Track all scores and get next level
const GamePage = ({ playerName }) => {
  const [isStartGame, setIsStartGame ] = useState(false);

    const handleView = () => {
      setIsStartGame(true)
    };
  return (
    <>
    {
      isStartGame ?
      (
        <GameScreen />
      ):(
        <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh" bg="green.200">
      <Text fontSize="2xl">Hello, {playerName}! Let's start the game.</Text>
      <Button colorScheme="green" onClick={handleView}>I'm ready</Button>
    </Box>
      )
    }
    
    </>
    
  );
};

export default GamePage;
