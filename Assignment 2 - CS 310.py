#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Stefana Ciustea
# Assignment 2 - CS 310 at BC
# 10/23/2022

import numpy as np

def maze_solver(maze):
    np_maze = np.array(maze)
    path = []
    direction = 1  # 1=right, -1=left, 2=up, -2=down
    position = (0, 0)
    
    while in_maze(position, np_maze):
        position_y, position_x = position
        path.append(position)
        
        if np_maze[position_y, position_x] == -1:
            direction = -direction  # mirror reflection
            
        position = move(direction, position)
        
    return path

def move(direction, position):
    position_y, position_x = position
    if direction == 1:
        position_x += 1
    elif direction == -1:
        position_x -= 1
    elif direction == 2:
        position_y -= 1
    elif direction == -2:
        position_y += 1
    return (position_y, position_x)

def in_maze(position, np_maze):
    shape_y, shape_x = np_maze.shape
    position_y, position_x = position
    in_x_axis = 0 <= position_x < shape_x
    in_y_axis = 0 <= position_y < shape_y
    return in_x_axis and in_y_axis

# Example maze
maze = [
    [0, 0, 0, -1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [-1, 0, 0, 0]
]

path = maze_solver(maze)
print(path)


# In[ ]:




