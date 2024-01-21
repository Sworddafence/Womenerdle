import { useState } from "react";
import Fireworks from "react-canvas-confetti/dist/presets/fireworks";

export default function Confetti() {
  return (
      <Fireworks onInit={({ conductor }) => {
        conductor.shoot();
        conductor.shoot();
      }} />
  );
}