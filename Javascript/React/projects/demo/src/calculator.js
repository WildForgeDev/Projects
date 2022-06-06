import React, {Component} from "react";
import './css/style.css';

class Calculator extends Component{
    render(){
        return(
            <div class="calculator">
                <div class="calculator-body">
                    <div class="calculator-container-screen">
                        <h3 class="result">0</h3>
                    </div>
                    <div class="calculator-container-buttons">
                        <table class="buttons">
                            <tr>
                                <td>1</td>
                                <td>2</td>
                                <td>3</td>
                                <td>+</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td>5</td>
                                <td>6</td>
                                <td>-</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td>8</td>
                                <td>9</td>
                                <td>X</td>
                            </tr>
                            <tr>
                                <td>0</td>
                                <td>=</td>
                                <td>C</td>
                                <td>/</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        );
    }
}

export default Calculator;



