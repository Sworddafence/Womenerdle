'use client';

import { Text } from "@mantine/core";

// fetch either text or image
// display first hint
export default function Hint({ hint }) {
    return (
        <div className="flex flex-col items-center justify-center">
            <Text>{hint}</Text>
        </div>
    )
}