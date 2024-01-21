import "./globals.css";
import "@mantine/core/styles.css";
import '@mantine/notifications/styles.css';

import React from "react";import { MantineProvider, ColorSchemeScript, Title } from "@mantine/core";
import { Notifications } from "@mantine/notifications";

export const metadata = {
  title: "Shenius",
  description: "game",
};


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <ColorSchemeScript defaultColorScheme="dark"/>
        <link rel="shortcut icon" href="/favicon.svg" />
        <meta
          name="viewport"
          content="minimum-scale=1, initial-scale=1, width=device-width, user-scalable=no"
        />
      </head>
      <body>
        <MantineProvider defaultColorScheme="dark">
          <Notifications/>
          <div className="flex flex-col items-center">
            <Title className="pt-8 pb-4 flex">Shenius</Title>
          </div>
          {children}
        </MantineProvider>
      </body>
    </html>
  );
}
