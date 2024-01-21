'use client';

import { Autocomplete, Box, Button, Skeleton, Title } from "@mantine/core";
import Hint from "./components/Hint";
import { useState, useEffect } from "react";
import { notifications } from "@mantine/notifications";
import Image from "next/image";
import RootLayout from "./layout";

export default function HomePage() {
  const [hints, setHints] = useState([]);
  const [hintIndex, setHintIndex] = useState(0);
  const [hint, setHint] = useState("");

  const [womanList, setWomanList] = useState([]);

  const [image, setImage] = useState("");

  const [answer, setAnswer] = useState("");
  const [guess, setGuess] = useState("");

  const [gameOver, setGameOver] = useState(false);

  useEffect(() => {
    fetch("http://localhost:5000/hints")
        .then((res) => res.json())
        .then((data) => {
          setHints(data.array)
          setHint(data.array[0])
          setHintIndex(0)

          setAnswer(data.name)

          setImage(data.picture)
        });

    fetch("http://localhost:5000/lists")
        .then((res) => res.json())
        .then((data) => setWomanList(data.array));

    }, []);




  const check = (e) => {
    e.preventDefault()
    if (guess === answer) {
      notifications.show({ title: "Correct!", message: "You guessed correctly!", color: "green" });
      setHintIndex(5)
      setGameOver(true)
    } else {
      if (hintIndex < 4) {
        notifications.show({ title: "Wrong!", message: "You guessed wrong! Try again!", color: "red" });
        setHintIndex(hintIndex + 1)
        setHint(hints[hintIndex + 1])
      } else {
        if (!gameOver) {
          notifications.show({ title: "Game over.", message: "Womp womp", color: "red" });
          setGameOver(true)
        }
      }
    }
  }

  const blur = ['blur-lg', 'blur-md', 'blur', 'blur-sm', 'blur-none'][hintIndex]

  return     <Box bg="#55423d" className="rounded-[5px] p-8 max-w-[800px] mx-auto mt-8 border border-black border-solid border-2">
  <main className="flex min-h-screen flex-col items-center p-8">
  <Box w={{ base: 200, sm: 400, lg: 470 }} bg="#e78fb3" className="rounded-[5px] p-8 max-w-[100000px] mx-auto mt-8">
    <Title className="pb-4 text-center"style={{fontFamily: 'proxima-nova, sans-serif', fontSize: '80', color: '#fffffe' }}>Shenius</Title>
    {/* <Skeleton width={300} visible={image == ""}>
      <Image src={'/pictures/' + image} width={300} height={300} radius = {100} className={'duration-100 my-4 rounded-full' + blur}/>
    </Skeleton> */}
    <Skeleton width={300} visible={image == ""} className="mx-auto">
  <Image
    src={'/pictures/' + image}
    width={300}
    height={300}
    className={'duration-100 my-4 rounded-[15px] ' + blur}
    style={{ overflow: 'hidden', border: '4px solid black' }}
  />
</Skeleton>
</Box>
    <Box bg="#fff3ec" className="rounded-[10px] p-4 m-4 text-center border border-black border-solid border-2" maw={500}>
      <Hint hint={hint} style = {{color: 'blue'}}></Hint>
    </Box>
  
    <div>
  {
    [1, 2, 3, 4, 5].map(i => {
      if (i <= hintIndex + 1)
        return <Button
          variant="outline"
          color="#ffc0ad"
          key={i}
          className="mx-3.5 my-3"
          radius={20}
          onClick={() => setHint(hints[i - 1])}
          style={{ fontSize: '1.2rem', width: '4rem', height: '3rem', borderWidth: '3px' }} // Adjust the font and button size
        >
          {i}
        </Button>
      else
        return <Button key={i} className="mx-3-3.5 my-3" radius={1000} disabled style={{ fontSize: '1.5rem' }}>{i}</Button>
    })
  }
</div>

    <form className="flex flex-row items-end m-4" onSubmit={check}>
      <Autocomplete data={womanList.sort()} limit={6} placeholder="Guess a historic woman!" onChange={setGuess} disabled={gameOver}
       styles={{
        input: {
          color: '#271c19',
          backgroundColor: '#ffc0ad', 
          borderRadius: '5px', // Make the input round
        },
      }}/>
      {/* <Button color = "blue" onClick={check} disabled={gameOver}>Check</Button> */}
      <Box mt={3} bg="#e78fb3"> {/* Add a margin-top to separate the "Check" button */}
  <Button
    color="blue"
    onClick={check}
    disabled={gameOver}
    style={{
      border: '2px solid black', // Add a border to the button
      borderRadius: '5px', // Make the button round
      padding: '8px 16px', // Adjust padding as needed
    }}
  >
    Check
  </Button>
</Box>

    </form>

    {gameOver &&
      <Button onClick={() => window.location.reload()} className="m-4">Next Game</Button>
    }
  </main>
  </Box>;
}