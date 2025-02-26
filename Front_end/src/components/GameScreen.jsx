import React, { useState, useEffect } from 'react';
import { Box, Button, Input, Text, VStack } from '@chakra-ui/react';


const GameScreen = () => {
  const [minScore, setMinScore] = useState(3);
  const [questions, setQuestions] = useState([]);
  const [index, setIndex] = useState(0);
  const [currentAnswer, setCurrentAnswer] = useState(0);
  const [currentScore, setCurrentScore] = useState(0);
  const [passedIndex, setPassedIndex] = useState([]);
  const [showScore, setShowscore] = useState(false);
  const [subLevel, setSubLevel] = useState(1);
  const [error, setError] = useState(null);
  const [gameOver, setGameOver] = useState(false);

// set url params dynamically - name & age in local storage - sublevel in state
  const getQuestions = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/api/questions?player_name=Nkululeko&age=8&sub_level=1`);
        const data = await response.json();
        console.log('API',data?.questions)
        if (response.ok) {
          setMinScore(data?.min_Score)
          setQuestions(data?.questions)
          setError(null);
        } else {
          setError('Failed to fetch the level. Please try again.');
        }
      } catch {
        setError('Failed to fetch the level. Please try again.');
      }
  };

  useEffect(() => {
    getQuestions()
 },[]);

 //create gameover and score view 
 // gameover view should have a button to restart / should reset all state values to default and clear local storage
 // button on scroll view should reset flags that are used to show both gameover and scoreview probably if/else statements
 //on return section
  const handleQuestion = () => {
    const rightAnswer = questions[index].answer;
    // if answer is correct increase score
    if (currentAnswer == rightAnswer) {
      setCurrentScore((prevScore) => prevScore + 1);
      setPassedIndex((prevPassIndex) => [...prevPassIndex, index])
    }
    const islastQuestion = (questions[questions.length-1]).question == questions[index]

    if (islastQuestion){ 
      setShowscore(true)
      if (currentScore <= minScore)
        setSubLevel((prevSubLevel) => prevSubLevel + 1)
      else
        setGameOver(true)

    }else{
      setIndex((prevIndex) => prevIndex + 1)
    }

    

  }

  return (
      <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh" bg="blue.200">
        <Text fontSize="3xl" fontWeight="bold" mb={4}>{questions[index]?.question ?? "Oops! Looks like something went wrong"}</Text>
        
          <VStack spacing={4} align="center">
          <Input
            placeholder="Answer"
            value={currentAnswer}
            onChange={(e) => setCurrentAnswer(e.target.value)}
            size="md"
            width="250px"
          />
          {/* {nameError && <Text color="red.500">{nameError}</Text>} */}
          <Button colorScheme="green" onClick={handleQuestion}>Submit</Button>
        </VStack>
      </Box>
  )
};

export default GameScreen;
