import React, {PureComponent, useEffect, useState, useContext} from 'react';
import logo from './logo.svg';
import pizza from './pizza.svg';
import salad from './salad.svg';
import burger from './burger.svg';

import './App.css';
import MapChart from "./MapChart";
import Map from "./Map";

function Filters(props) {
  const {data} = props;
  const [selected, setSelected] = useState("");

  return data.map( filter => {
    return (
        <div className={`foodFilter ${selected === filter.name ? "selected" : ""}`} onClick={() => {
          
          props.setFoodType(filter.name)
          setSelected(filter.name);
        }}>
          <img src={filter.image} width="60" height="60"/>
        </div>
    );
  });
}

function App() {
  const foodTypes = [
    {
      name: "1",
      image: pizza
    }, {
      name: "2",
      image: salad
    }, {
      name: "0",
      image: burger
    }
  ];
  const [foodType, setFoodType] = useState("");

  return (
    <div className="App">
      <header className="App-header">
        <Filters data={foodTypes} setFoodType={setFoodType}/>
      </header>
      <Map foodType={foodType}/>
    </div>
  );
}

export default App;
