import random
import os
import time
import keyboard
import threading

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

snakeCharacter = "S"
appleCharacter = "O"

snake = [(0, 2)]
xVel = 1
yVel = 0
display = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
]

updateSnake = False
running = True

def input():
    global xVel
    global yVel

    while True:
        key = keyboard.read_key()
        if key == "w":
            yVel = -1
            xVel = 0
        if key == "a":
            yVel = 0
            xVel = -1
        if key == "s":
            yVel = 1
            xVel = 0
        if key == "d":
            yVel = 0
            xVel = 1
        if key == "q":
            running = False
            return

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
    for j in range(BOARD_HEIGHT):
        buffer = ""
        for i in range(BOARD_WIDTH):
            buffer += display[j][i]
        print(buffer)

def main():
    inputThread = threading.Thread(target=input)
    inputThread.start()

    while running:
        update_snake()
        update_display()
        show_display()
        time.sleep(.5)
        os.system("cls")
        

main()
