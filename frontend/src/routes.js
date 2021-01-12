import React from "react";
import {Route} from 'react-router-dom'

import TodoList from "./containers/TodoListView";
import TodoDetail from "./containers/TodoDetailView";

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={TodoList} />
        <Route exact path='/:todoID' component={TodoDetail} />
    </div>
);

export default BaseRouter;
