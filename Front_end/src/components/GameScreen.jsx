import { useState } from 'react';
import PropTypes from 'prop-types';
import { TextInput, Button, Text, StyleSheet } from 'react-native';
import { VStack, Heading, Box } from '@chakra-ui/react';

const GameScreen = ({ name }) => {
  const [age, setAge] = useState('');
  const [level, setLevel] = useState(null);
  const [error, setError] = useState(null);

  const handleAgeSubmit = async () => {
    if (age) {
      try {
        const response = await fetch(`http://localhost:5000/api/level_by_age?age=${age}`);
        const data = await response.json();
        if (response.ok) {
          setLevel(data.level);
          setError(null);
        } else {
          setError('Failed to fetch the level. Please try again.');
        }
      } catch {
        setError('Failed to fetch the level. Please try again.');
      }
    }
  };

  return (
    <VStack style={styles.container} spacing={4} align="center" justify="center">
      <Heading>Hello, {name}!</Heading>
      <Box>
        <TextInput
          style={styles.input}
          placeholder="Enter your age"
          value={age}
          onChangeText={setAge}
        />
        <Button title="Submit Age" onPress={handleAgeSubmit} />
      </Box>
      {level !== null && (
        <Text>Your level is: {level}</Text>
      )}
      {error && (
        <Text style={styles.error}>{error}</Text>
      )}
    </VStack>
  );
};

GameScreen.propTypes = {
  name: PropTypes.string.isRequired,
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
  error: {
    color: 'red',
  },
});

export default GameScreen;
