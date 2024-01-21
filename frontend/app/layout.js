import "@mantine/core/styles.css";
import '@mantine/notifications/styles.css';

import React from "react";import { MantineProvider, ColorSchemeScript, createTheme, rem, Button, Autocomplete } from "@mantine/core";
import { Notifications } from "@mantine/notifications";

export const metadata = {
  title: "Shenius",
  description: "game",
};

import "./globals.css";

const theme = createTheme({
  fontFamily: 'proxima-nova, sans-serif',
  primaryColor: 'bright-pink',
  colors: {
    'bright-pink': ['#ffc0ad', '#ffc0adF', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad'],
    'blue': ['#ffc0ad', '#ffc0adF', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad', '#ffc0ad'],
    'red': ['#55423d', '#55423d', '#55423d', '#55423d', '#55423d', '#55423d', '#55423d', '#55423d', '#55423d', '#55423d'],
  },
  white: "#ffc0ad",
  black: "#271c19"

});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <MantineProvider theme={theme}/>
        <link rel="shortcut icon" href="/favicon.svg" />
        <meta
          name="viewport"
          content="minimum-scale=1, initial-scale=1, width=device-width, user-scalable=no"
        />
      </head>
      <body>
        <MantineProvider theme={theme}>
          <Notifications/>
          {children}
        </MantineProvider>
      </body>
    </html>
  );
}
