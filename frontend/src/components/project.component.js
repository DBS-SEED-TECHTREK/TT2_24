import React, {useEffect, useState} from 'react';
import DataTable from 'react-data-table-component';



// Token

export default function Dashboard({projectList=[]}) {

  const columns = [
    {
      name: 'Id',
      cell: row => row.id
    },
    {
        name: 'User_Id',
        sortable: true,
        selector: row => row.user_id
    },
    {
        name: 'Name',
        sortable: true,
        selector: row => row.name
    },
    {
        name: 'Description',
        sortable: true,
        selector: row => row.description
    },
    {
        name: 'Budget',
        sortable: true,
        selector: row => row.budget
    },
  ];


  
  return (
    <DataTable
        columns={columns}
        data ={[...Object.values(projectList)]}
        noHeader
        pagination
    />
)
}