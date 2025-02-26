import React, { useState } from 'react';
import { Box, Button, Input, Text, VStack } from '@chakra-ui/react';

// set name and age, then view game page
const WelcomePage = ({ onProceed }) => {
  const [toogleView, setToogleView] = useState(false);
  const [name, setName] = useState('');
  const [nameError, setNameError] = useState('');

  const [age, setAge] = useState('');
  const [ageError, setAgeError] = useState('');

  const handleName = () =>{
    if (name.length == 0) {
      setNameError('Please enter your name');
      return;
    }
    setToogleView(true)
  }

  const handleAge = async () => {
    if (age.length == 0) {
      
        setAgeError('Please enter your age');
        return;
    }

    if (name && age > 5)
    {
      // storename and age into local storage
      onProceed()
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh" bg="blue.200">
      <Text fontSize="3xl" fontWeight="bold" mb={4}>Welcome to the Arithmetic Drill!</Text>
      {!toogleView ? (
        <VStack spacing={4} align="center">
        <Input
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          size="md"
          width="250px"
        />
        {nameError && <Text color="red.500">{nameError}</Text>}
        <Button colorScheme="green" onClick={handleName}>Proceed</Button>
      </VStack>
      ):(
        <VStack spacing={4} align="center">
        <Input
          placeholder="Enter your age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          size="md"
          width="250px"
        />
        {ageError && <Text color="red.500">{ageError}</Text>}
        <Button colorScheme="green" onClick={handleAge}>Proceed</Button>
      </VStack>
      )}
    </Box>
  );
};

export default WelcomePage;
