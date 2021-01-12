import React from "react";
import axios from "axios";

import {Card} from 'antd'

class TodoDetail extends React.Component {

    state = {
        todo: {}
    }

    componentDidMount() {
        const todoID = this.props.match.params.todoID;
        axios.get(`http://127.0.0.1:8000/api/${todoID}`)
            .then(res => {
                this.setState({
                    todo: res.data
                });
                console.log(res.data)
            })
    }

    render() {
        return(
           <Card title={this.state.todo.title}>
               <p>{this.state.todo.description}</p>
           </Card>
        )
    }
}

export default TodoDetail;
