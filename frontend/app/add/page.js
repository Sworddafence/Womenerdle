'use client'

import { Box, Button, FileInput, Text, TextInput } from "@mantine/core";
import { useState } from "react";
import { FileUpload } from "tabler-icons-react";
// add a woman to the database
// need to add a name, picture, and hints
export default function Add() {
    const [name, setName] = useState("")
    const [picture, setPicture] = useState("")
    const [hint1, setHint1] = useState("")
    const [hint2, setHint2] = useState("")
    const [hint3, setHint3] = useState("")
    const [hint4, setHint4] = useState("")
    const [hint5, setHint5] = useState("")

    const handleSubmit = async e => {
        e.preventDefault()
        const formData = new FormData()
        formData.append("image", picture)
        let index = await fetch("http://localhost:5000/picture_upload", { method: "POST", body: formData })
            .then(res => res.text())
        fetch("http://localhost:5000/hints_upload", { method: "POST", body: JSON.stringify({
            name: name,
            hints: [hint1, hint2, hint3, hint4, hint5],
            id: index,
        }), headers: { "Content-Type": "application/json" } })
    }

    return (
        <Box className="flex flex-grow justify-center">
            <form className="flex flex-col gap-4">
                <TextInput label="Name" placeholder="Name" required style={{minWidth: '300px'}} onChange={e => setName(e.currentTarget.value)}/>
                <FileInput label="Picture" placeholder="Picture" required style={{minWidth: '300px'}} rightSection={<FileUpload/>} rightSectionPointerEvents="none" value={picture} onChange={setPicture}/>
                <TextInput label="Hint 1" placeholder="Hint 1" required style={{minWidth: '300px'}} onChange={e => setHint1(e.currentTarget.value)}/>
                <TextInput label="Hint 2" placeholder="Hint 2" required style={{minWidth: '300px'}} onChange={e => setHint2(e.currentTarget.value)}/>
                <TextInput label="Hint 3" placeholder="Hint 3" required style={{minWidth: '300px'}} onChange={e => setHint3(e.currentTarget.value)}/>
                <TextInput label="Hint 4" placeholder="Hint 4" required style={{minWidth: '300px'}} onChange={e => setHint4(e.currentTarget.value)}/>
                <TextInput label="Hint 5" placeholder="Hint 5" required style={{minWidth: '300px'}} onChange={e => setHint5(e.currentTarget.value)}/>
                <Button onClick={handleSubmit}>Submit</Button>
            </form>
        </Box>
    )
}