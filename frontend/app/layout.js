import "./globals.css";
import "@mantine/core/styles.css";
import '@mantine/notifications/styles.css';

import React from "react";import { MantineProvider, ColorSchemeScript } from "@mantine/core";
import { Notifications } from "@mantine/notifications";

export const metadata = {
  title: "Womenerdle",
  description: "game",
};


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <ColorSchemeScript defaultColorScheme="auto"/>
        <link rel="shortcut icon" href="/favicon.svg" />
        <meta
          name="viewport"
          content="minimum-scale=1, initial-scale=1, width=device-width, user-scalable=no"
        />
      </head>
      <body>
        <MantineProvider defaultColorScheme="auto">
          <Notifications/>
          {children}
        </MantineProvider>
      </body>
    </html>
  );
}
