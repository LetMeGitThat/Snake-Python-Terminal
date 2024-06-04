import random
import os
import time
import keyboard
import threading

BOARD_WIDTH = 25
BOARD_HEIGHT = 10
UPDATE_SPEED = 0.2

SNAKE_CHARACTER = "S"
APPLE_CHARACTER = "O"

snake = [(0, 2)]
xVel = 1
yVel = 0
display = [["#" if x == 0 or x == BOARD_WIDTH - 1 or y == 0 or y == BOARD_HEIGHT - 1 else " " for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

grow = False
running = True

def input():
    # handle input
    global xVel
    global yVel
    global running

    while True:
        if not running:
            break

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
    global running
    # add an element to the first position where the head should be and pop the table
    position = (snake[0][0]+xVel, snake[0][1]+yVel)
    if position[0] > BOARD_WIDTH - 2 or position[1] > BOARD_HEIGHT - 2 or position[0] < 1 or position[1] < 1:
        running = False
        return
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
    while True:
        x = random.randint(1, BOARD_WIDTH-2)
        y = random.randint(1, BOARD_HEIGHT-2)
        position = (x, y)
        for tail in snake:
            if tail[0] == x and tail[1] == y:
                continue
        break
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

        display = [["#" if x == 0 or x == BOARD_WIDTH - 1 or y == 0 or y == BOARD_HEIGHT - 1 else " " for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
        os.system("cls")
    print("Game Over, you scored: " + str(score))
        
start()