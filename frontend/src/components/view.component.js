import React, {useState, useEffect}  from 'react';
import PropTypes from 'prop-types';

// Rough idea of the page, unable to run.
const [project, setProject] = useState(null);

useEffect(() => {
    getExpense();

async function getExpense() {
    return fetch('http://localhost:5000/api/get_expense')
    .then(response => response.json())
    .then(data => data.json())
   }
   
   setProject(data) ;
}, []);

return(
    <div className="view-wrapper">
      <h1>View Expense</h1>
    
    {/* looping the expenses in the project*/}
    {expenses.map((expenses, index) => (
    <div key={index}>
        <p>{project.data}</p>

    </div>
    ))}
    </div>
    )
