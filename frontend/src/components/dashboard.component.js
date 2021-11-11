import React, {useEffect, useState} from 'react';
import axios from 'axios';
import Login from "./login.component";
import Project from "./project.component"


// Token

export default function Dashboard({token}) {
  const [projectList, setProjectList] = useState()

  const fetchData = async(token) =>{
    console.log(token)
    axios({
      method: 'post',
      url: "http://localhost:5000/api/get_projects_by_user_id",
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Headers': 'x-access-tokens',
        'x-access-tokens': token
      }
    }).then(res => {
            console.log(res.data["project"])
            setProjectList(res.data["project"])
        })
        .catch((error)=>{
            console.log(error)
        })
  }

  useEffect(() => {fetchData(token)},[])

  return (
    <Project projectList={projectList}/>
  ) 
}