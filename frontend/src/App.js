import React, {Component} from 'react'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap/dist/js/bootstrap.bundle.min';

// Components 
import Login from "./components/login.component";
import DashboardPage from "./components/dashboard.component";
import ExpensePage from "./components/expense.component";

// Token
import useToken from './components/useToken';

// Main app
function App() {
  // Token Auth
  const { token, setToken } = useToken();

  // TODO: Add back for authentication testing
  // if(!token) {
  //   return <Login setToken={setToken} />
  // }

  // App
  return (
    <Router>
    <div className="container-fluid">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div className="navbar-nav">
                  <Link to="/" className="navbar-brand">Home</Link>
                  <Link to="/expense" className="nav-item nav-link">Expense</Link>
              </div>
          </div>
      </nav>

        <Route path="/" exact component={DashboardPage} />
        <Route path="/expense" exact component={ExpensePage} />
    </div>

     
  </Router>
  );

}

export default App;
