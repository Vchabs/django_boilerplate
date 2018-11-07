import React, { Component } from 'react';
//group your files so you know where they are
//try and make them independent
class Finances extends Component {

  constructor(props) {
	super(props);    
    
  }

  render(){
  	var debtClass="red";
  	if (this.props.deficit) {
  		if (this.props.deficit >=0){
  			debtClass = "blue"
  		}
  	}
  	return (
  			<div className="finances">
  				<h2 id="finances-title">Monthly Finances </h2>
  				<div className="fhealth">Income: <span>{this.props.income}</span></div>
  				<div className="expenses">Expenses: <span>{this.props.expenses}</span></div>
  				<div className="debt">Balance/Deficit: <span className={debtClass}>{this.props.deficit}</span></div>
  				<div className="fhealth">Accumulated Savings: <span>{this.props.savings}</span></div>
  				
  			</div>

  		);
  }
}


export default Finances;