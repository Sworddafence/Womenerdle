'use client';

import { Autocomplete, Box, Button, Title } from "@mantine/core";
import Hint from "./components/Hint";
import { useState, useEffect } from "react";
import { notifications } from "@mantine/notifications";

export default function HomePage() {
  const [hints, setHints] = useState([]);
  const [hintIndex, setHintIndex] = useState(0);
  const [hint, setHint] = useState("");

  const [womanList, setWomanList] = useState([]);


  const [answer, setAnswer] = useState("");
  const [guess, setGuess] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/hints")
        .then((res) => res.json())
        .then((data) => {
          setHints(data.array)
          setHint(data.array[0])
          setHintIndex(0)

          setAnswer(data.name)
        });

    fetch("http://localhost:5000/lists")
        .then((res) => res.json())
        .then((data) => setWomanList(data.array));

    }, []);


  const check = (e) => {
    e.preventDefault()
    if (guess === answer) {
      notifications.show({ title: "Correct!", message: "You guessed correctly!", color: "green" });
    } else {
      if (hintIndex < 4) {
        notifications.show({ title: "Wrong!", message: "You guessed wrong! Try again!", color: "red" });
        setHintIndex(hintIndex + 1)
        setHint(hints[hintIndex + 1])
      } else {
        notifications.show({ title: "Game over.", message: "Womp womp", color: "red" });
      }
    }
  }

  return <main className="flex min-h-screen flex-col items-center p-8">
    <Title className="pb-4">Womenerdle</Title>
    <Box bg="dark.9" className="rounded p-4 m-4">
      <Hint hint={hint}></Hint>
    </Box>
    <div>
      {
        [1, 2, 3, 4, 5].map(i => {
          if (i <= hintIndex + 1)
            return <Button key={i} className="mx-2 my-4" radius={1000} onClick={() => setHint(hints[i - 1])}>{i}</Button>
          else
            return <Button key={i} className="mx-2 my-4" radius={1000} disabled>{i}</Button>
        })
      }
    </div>

    <form className="flex flex-row items-end m-4">
      <Autocomplete data={womanList.sort()} limit={6} placeholder="Guess a historic woman!" onChange={setGuess}/>
      <Button onClick={check}>Check</Button>
    </form>

  </main>;
}