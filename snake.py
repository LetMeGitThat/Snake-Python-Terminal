import random
import os
import time

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

snakeCharacter = "S"
appleCharacter = "O"

snake = [(0, 2)]
xVel = 1
yVel = 0
display = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

updateSnake = False

def input():
    pass

def update_snake():
    # add an element to the first position where the head should be and pop the table
    position = (snake[0][0]+xVel, snake[0][1]+yVel)
    if position[0] >= BOARD_WIDTH or position[1] >= BOARD_HEIGHT or position[0] < 0 or position[1] < 0:
        print("player has hit a wall end it") 
        return False
    snake.insert(0, position)

def update_display():
    for position in snake:
        display[position[1]][position[0]] = snakeCharacter

def show_display():
    for j in range(5):
        buffer = ""
        for i in range(5):
            buffer += display[j][i]
        print(buffer)

def main():
    while True:
        input()
        update_snake()
        update_display()
        show_display()
        time.sleep(.5)
        

main()
