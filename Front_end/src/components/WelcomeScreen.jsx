import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { TextInput, Button, StyleSheet } from 'react-native';
import { Box, VStack, Heading } from '@chakra-ui/react';

// set name and age, then view game page
const WelcomeScreen = ({ onNext }) => {
  const [name, setName] = useState('');

  const handleProceed = () => {
    if (name) {
      onNext(name);
    }
  };

  return (
    <VStack style={styles.container} spacing={4} align="center" justify="center">
      <Heading>Welcome to the Game</Heading>
      <Box>
        <TextInput
          style={styles.input}
          placeholder="Enter your name"
          value={name}
          onChangeText={setName}
        />
        <Button title="Proceed" onPress={handleProceed} />
      </Box>
    </VStack>
  );
};

WelcomeScreen.propTypes = {
  onNext: PropTypes.func.isRequired,
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});

export default WelcomeScreen;
