import './App.css';
import { useState, useEffect } from "react";
import LoginForm from "./LoginForm";
import SummaryForm from "./SummaryForm";

function App() {
  const [userData, setUserData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/data")
    .then(resp => resp.json())
    .then(resp => {setUserData(resp); console.log("SUCCESS!"); console.log(resp); console.log(resp[0]["created_date"])})
    .catch(error => {console.log(error); console.log("This is generating the message")})
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Article Summarizer</h1>
        <h2>React/Flask/LLM project developed by Andrew Strickland</h2>
      </header>
      <LoginForm></LoginForm>
      <SummaryForm userData={userData}></SummaryForm>
    </div>
  );
}
export default App;
