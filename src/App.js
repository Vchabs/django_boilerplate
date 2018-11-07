import React, { Component } from 'react';
import logo from './logo.svg';
import Finances from './components/finances/Finances';
import Scene from './components/scenario/Scene';


import './css/App.css';


// -have an expense thing that updates each month

class App extends Component {
  constructor(props){
    super(props);

    // You set up your state here, be it initial or not
    this.state = {};
    //bind any of your functions like this if you're using this method
    this.func1 = this.func1.bind(this);
    this.func2 = this.func2.bind(this);
  }


  componentDidMount() { 
    // in here you set the initial state or fetch if you need to
    // fetch is essentially an ajax call and this is called once 
    this.setState({"id": "whatever"});
  }


  func1() {
    // you also can have regular javascript variables added
    // this is a regular javascript funciton and you can do whatever
    
    // do stuff here, 
    // you can call this.setState if needed but you don't have to unless you want to
  }

  func2(money){
    // same here
  }



  render() {
    // In react this HAS to be a list of html or components, and each of them needs a 
    // prop key with a different value 
    var monthHolder = [(<div key={1}>YO</div>)]
   
    var cost;
    var item, v;
    var income, expenses, savings, deficit;
    // This returns what this class renders and each of the items in the {} are react/js variables
    // the parameters in each thing are called props and can be referenced by this.props.NAME_HERE
    // you can do class="blah blah" and it'll work but for it not to be confused with props 
    // it's better to do className="blah blah" because it gets cold at night.
    // You can also pass in fucntions all the way down the line (this.next)
    return (
      <div className="App">
      <div className="game">
        <Finances expenses={expenses} income={income} savings={savings} deficit={deficit}/>
        <Scene Item={item} Verbiage={v} cost={cost} next={this.next} />
      </div>
        <div className="month-holder">
          {monthHolder}
        </div>
      </div>
    );
  }
}

//this is what you're exporting for other things to use
export default App;
