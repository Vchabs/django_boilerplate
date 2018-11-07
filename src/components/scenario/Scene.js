import React, { Component } from 'react';

//thisis what we caused 
class Scene extends Component {

  constructor(props) {
	super(props);
	this.no = this.no.bind(this);
	this.yes = this.yes.bind(this);    
    
  }

  no(e) {
    // this is meant for a button so im doing this
  	e.preventDefault();
    //As I said before u can pass in functions
  	//this.props.next(0)
  }

  yes(e) {
    e.preventDefault();
  	//this.props.next(this.props.cost)
  }


  render() {
    // look at your js console 
  	console.log(this.props)
    return (
    	<div> ANYTHING HERE  </div>
    );
  }
}

export default Scene;