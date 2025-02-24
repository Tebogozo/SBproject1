import React from "react";
import WelcomeScreen from "./components/WelcomeScreen.jsx"

const onNext = (name) => {console.log(name)};

function App() {

  return(
   <WelcomeScreen onNext={onNext}/>
  )
}

export default App
