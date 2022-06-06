import React, { Component } from 'react';
import HighScore from './HighScore';
import './css/style.css';
import Calculator from './calculator';

class Application extends Component {
    constructor(props){
        super(props);

        this.state = {
            count: 0,
            overTen: false
        }
    }

    // componentWillMount(props, state){

    // }

    // componentDidMount(props, state){
    //     console.log("mounted with", props, state);
    // }

    // componentWillReceiveProps(props){

    // }

    // componentWillUpdate(props, state){
    //     if(this.props.name !== props.name){
    //         // do something
    //     }
    // }

    // componentDidUpdate(props, state){

    // }

    handleClick = () => {
        this.setState({
            count: this.state.count + 1
        })
    }

    componentDidUpdate(props, state){
        if(this.state.count > 10 && this.state.count !== state.count && !this.state.overTen){
            console.log('updating over ten');
            this.setState({overTen: true});
        }
    }

    resetCount = (e) => {
        console.log("Event is", e)
        this.setState({
            count: 0,
            overTen: false
        });
    }

    render() {
        let {count} = this.state;
        return (<div> 
                    <h1>You clicked the button {count} times.</h1>
                    <HighScore 
                        overTen={this.state.overTen}
                        onReset={this.resetCount}
                    />
                    <span><button onClick={() => this.handleClick()}>Click Me</button></span>
                    <Calculator 
                    />
                </div>
        );
    }

}

export default Application;