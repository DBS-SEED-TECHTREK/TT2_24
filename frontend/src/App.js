import React from 'react';
import './App.css';
// npm install react-router-dom
import { BrowserRouter, Route, Routes } from 'react-router-dom';
// Components 
import Login from "./components/login.component";

// Token
import useToken from './components/useToken';

// Main app
function App() {
  // Token Auth
  const { token, setToken } = useToken();
  if(!token) {
    return <Login setToken={setToken} />
  }

  // App
  return (
    <div className="wrapper">
      <h1>Project Expense App</h1>
      <BrowserRouter>
        <Routes>
          {/* <Route path="/Dashboard">
            <Dashboard />
          </Route> */}
        </Routes>
      </BrowserRouter>
    </div>
  );

}

export default App;
