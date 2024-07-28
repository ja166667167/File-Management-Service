import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const backendHost = import.meta.env.VITE_BACKEND_ENDPOINT;
  console.log(backendHost);
  return <div>Env: {backendHost}</div>;
}

export default App;
