import React from 'react'

import { List, Avatar } from 'antd';


const Todo = (props) => {
    return (
        <List
            itemLayout="horizontal"
            dataSource={props.data}
            renderItem={item => (
                <List.Item>
                    <List.Item.Meta
                        avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"/>}
                        title={<a href={`/${item.id}`}>{item.title}</a>}
                        description={item.state}
                    />
                    {item.description}
                </List.Item>
            )}
        />
    )
}

export default Todo
