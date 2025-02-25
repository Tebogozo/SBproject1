import React from 'react';
import { Box, Text } from '@chakra-ui/react';

const GamePage = ({ playerName }) => {
  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh" bg="green.200">
      <Text fontSize="2xl">Hello, {playerName}! Let's start the game.</Text>
    </Box>
  );
};

export default GamePage;
