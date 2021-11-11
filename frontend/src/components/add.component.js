import React, {useState}  from 'react';
import PropTypes from 'prop-types';
import Select from 'react-select';
import NumberFormat from 'react-number-format';

// Rough idea of the page, unable to run.
async function addExpense(credentials) {
    return fetch('http://localhost:5000/api/add_expense', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers': 'x-access-tokens',
        'x-access-tokens': token
      },
      body: JSON.stringify({
        Add();
      })
    })
      .then(data => data.json())
   }
   

export default function Add({token}) {
  const [name, setName] = useState();
  const [categoryId, setCategoryId] = useState();
  const [amount, setAmount] = useState();
  const [description, setDescription] = useState();
  const handleSubmit = async e => {
    e.preventDefault();
  }

  // get from api but not sure how
  const options = [
    { value: '1', label: 'Production' },
    { value: '2', label: 'Operation' },
    { value: '3', label: 'Financial' },
    { value: '4', label: 'Vendor' },
    { value: '5', label: 'Manpower' },
    { value: '6', label: 'Software' },
    { value: '7', label: 'Hardware' },
  ]

  return(
    <div className="add-wrapper">
      <h1>Add Expense</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Expense Name</p>
          <Select options={options} onChange={e => setName(e.target.value)}/>
        </label>
        <label>
          <p>Expense Type</p>
          <input type="select" onChange={e => setCategoryId(e.target.value)}/>
        </label>
        <label>
          <p>Expense Amount</p>
          <input type="text" pattern="[0-9]+(\.[0-9][0-9]?)?" onChange={e => setAmount(e.target.value)}/>
        </label>
        <label>
          <p>Description</p>
          <input type="textarea" onChange={e => setDescription(e.target.value)}/>
        </label>
        
        <div>
          <button type="submit">Add</button>
        </div>
      </form>
    </div>
  )
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired
}