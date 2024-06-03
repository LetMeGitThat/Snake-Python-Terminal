import random
import os

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

snakeCharacter = "S"
appleCharacter = "O"

snake = [(5, 5)]
xVel = 1
yVel = 0
display = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1] 
]

updateSnake = False

def input():
    pass

def update_snake():
    # add an element to the first position where the head should be and pop the table
    position = (snake[0][0]+xVel, snake[0][1]+yVel)
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

main()
