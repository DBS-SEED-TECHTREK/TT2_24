import React, {useEffect} from 'react';
import axios from 'axios';


import Login from "./login.component";


// Token
import useToken from './useToken';

export default function Dashboard({token}) {
  const fetchData = async(token) =>{
    console.log(token)
    var config = {
      headers: { "x-access-token": token, }
    }
    return await axios.post("http://localhost:5000/api/get_projects_by_user_id",
      config
      )
        .then(res => {
            console.log(res.data)
        })
        .catch((error)=>{
            console.log(error)
        })
  }
  fetchData(token)


  return(
      <div className="container">
          <h2>Dashboard</h2>
          <div></div>
      </div>
  );
}