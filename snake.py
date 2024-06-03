import random
import os
import time
import keyboard
import threading

BOARD_WIDTH = 10
BOARD_HEIGHT = 10
UPDATE_SPEED = 0.2

SNAKE_CHARACTER = "S"
APPLE_CHARACTER = "O"

snake = [(0, 2)]
xVel = 1
yVel = 0
display = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

grow = False
running = True

def input():
    # handle input
    global xVel
    global yVel
    global running

    while True:
        key = keyboard.read_key()
        if key == "w" and yVel != 1:
            yVel = -1
            xVel = 0
        if key == "a" and xVel != 1:
            yVel = 0
            xVel = -1
        if key == "s" and yVel != -1:
            yVel = 1
            xVel = 0
        if key == "d" and xVel != -1:
            yVel = 0
            xVel = 1
        if key == "q":
            running = False
            return

def update_snake():
    global grow
    # add an element to the first position where the head should be and pop the table
    position = (snake[0][0]+xVel, snake[0][1]+yVel)
    if position[0] >= BOARD_WIDTH or position[1] >= BOARD_HEIGHT or position[0] < 0 or position[1] < 0:
        return False
    snake.insert(0, position)

    # do not pop if we eat an apple
    if not grow:
        snake.pop()
    grow = False

def update_display(applePosition):
    # display the apple
    display[applePosition[1]][applePosition[0]] = APPLE_CHARACTER

    # display the snake
    for position in snake:
        display[position[1]][position[0]] = SNAKE_CHARACTER

def show_display():
    # show the display with a buffer
    for j in range(BOARD_HEIGHT):
        buffer = ""
        for i in range(BOARD_WIDTH):
            buffer += display[j][i]
        print(buffer)

def place_apple():
    x = random.randint(0, BOARD_WIDTH-1)
    y = random.randint(0, BOARD_HEIGHT-1)
    position = (x, y)
    return position

def self_collision():
    first = True

    for tail in snake:
        if not first and snake[0][0] == tail[0] and snake[0][1] == tail[1]:
            return True
        first = False

def start():
    global display
    global grow
    inputThread = threading.Thread(target=input)
    inputThread.start()

    score = 0

    applePosition = place_apple()

    while running:
        if snake[0][0] == applePosition[0] and snake[0][1] == applePosition[1]:
            score += 1
            grow = True
            applePosition = place_apple()
        
        update_snake()
        selfCollision = self_collision()

        if selfCollision:
            break
        update_display(applePosition)
        show_display()

        time.sleep(UPDATE_SPEED)

        display = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        os.system("cls")
    print("Game Over, you scored: " + str(score))
        
        
        

start()
