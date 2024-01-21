'use client';

import { Autocomplete, Box, Button, Skeleton, Title } from "@mantine/core";
import Hint from "./components/Hint";
import { useState, useEffect } from "react";
import { notifications } from "@mantine/notifications";
import Image from "next/image";

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

  return <main className="bg-[#55423d] flex min-h-screen flex-col items-center p-8">
    <Title className="text-[#fffffe] pb-4">Shenius</Title>
    <Skeleton width={300} visible={image == ""}>
      <Image src={'/pictures/' + image} width={300} height={300} className={'duration-100 my-4 ' + blur}/>
    </Skeleton>
    <Box bg="blue" className="rounded p-4 m-4 text-center" style={{borderwidth: '3px', bordercolor: '#271c19', color:"#271c19"}} maw={500}>
      <Hint hint={hint}></Hint>
    </Box>
    <div>
      {
        [1, 2, 3, 4, 5].map(i => {
          if (i <= hintIndex + 1)
            return <Button key={i} className="mx-2 my-4" style={{borderWidth: '3px', borderColor: '#271c19', color:"#271c19"}} radius={1000} onClick={() => setHint(hints[i - 1])}>{i}</Button>
          else
            return <Button key={i} className="mx-2 my-4 text-red" bg="#55423d" style={{borderWidth: '3px', borderColor: '#271c19', color:"#fff3ec"}} radius={1000} disabled>{i}</Button>
        })
      }
    </div>

    <form className="flex flex-row items-end m-4" onSubmit={check}>
      <Autocomplete data={womanList.sort()} limit={6} placeholder="Guess a historic woman!" onChange={setGuess} disabled={gameOver}/>
      <Button onClick={check} disabled={gameOver}>Check</Button>
    </form>

    {gameOver &&
      <Button onClick={() => window.location.reload()} className="m-4">Next Game</Button>
    }
  </main>;
}