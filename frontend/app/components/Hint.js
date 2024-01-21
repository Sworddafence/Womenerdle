'use client';

import { Skeleton, Text } from "@mantine/core";

// fetch either text or image
// display first hint
export default function Hint({ hint }) {
    return (
        <div className="flex flex-col items-center justify-center">
            { hint == "" ?
                <Skeleton height={12} width={300} animate={false}/>
                : <Text>{hint}</Text>
            }
        </div>
    )
}