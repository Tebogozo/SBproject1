import React, { useState } from 'react';
import { Box, Button, Input, Text, VStack } from '@chakra-ui/react';

const WelcomePage = ({ onProceed }) => {
  const [name, setName] = useState('');
  const [error, setError] = useState('');

  const handleProceed = async () => {
    if (!name) {
      setError('Please enter your name');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/api/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name }),
      });

      if (response.ok) {
        onProceed(name);
      } else {
        setError('Failed to start game. Try again.');
      }
    } catch (error) {
      setError('Server error. Please check your connection.');
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh" bg="blue.200">
      <Text fontSize="3xl" fontWeight="bold" mb={4}>Welcome to the Arithmetic Drill!</Text>
      <VStack spacing={4} align="center">
        <Input
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          size="md"
          width="250px"
        />
        {error && <Text color="red.500">{error}</Text>}
        <Button colorScheme="green" onClick={handleProceed}>Proceed</Button>
      </VStack>
      <Button position="absolute" bottom={4} left={4} colorScheme="red" onClick={() => window.close()}>
        Exit
      </Button>
    </Box>
  );
};

export default WelcomePage;
