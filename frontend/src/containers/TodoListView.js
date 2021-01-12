import React from "react";
import Todo from "../components/Todo";
import axios from "axios";

class TodoList extends React.Component {

    state = {
        todos: []
    }

    componentDidMount() {
        axios.get("http://127.0.0.1:8000/api/")
            .then(res => {
                this.setState({
                    todos: res.data
                });
                console.log(res.data)
            })
    }

    render() {
        return(
            <Todo data={this.state.todos}/>
        )
    }
}

export default TodoList;
