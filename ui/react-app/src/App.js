import './App.css'
import React, { useState, useEffect } from 'react';
import TableBody from './TableBody'
import TableHeaders from './TableHeaders'

function App() {
  const [orders, setOrders] = useState([]);

   useEffect(() => {
    fetch('http://localhost:5000/orders')
       .then((response) => response.json())
       .then((data) => {
          console.log(data);
          setOrders(data);
       })
       .catch((err) => {
          console.log(err.message);
       });
  }, []);

  return (
    <div>
      <table id="orderTable">
        <thead>
          <TableHeaders/>
        </thead>
        <TableBody jsonData={orders}/>
      </table>
    </div>
  );
}

export default App;
