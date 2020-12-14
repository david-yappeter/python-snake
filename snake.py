import pygame
from pygame.locals import *
import random

# Generate Food Dot
def GenerateFood():
    global screen, add
    global height, width
    global startX, startY
    global positionHistory
    RED = (255, 0, 0)

    while True:
        w = random.randint(0, height - add)
        h = random.randint(0, width - add)
        w -= w % add
        h -= h % add

        flag = 1
        for x in positionHistory:
            if x == (w,h):
                flag = 0

        if flag:
            break

    pygame.draw.rect(screen, RED, pygame.Rect(w, h, add, add))
    pygame.display.update()

    return w, h

def PositionAppend(positionArray, direction):
    global snakeLen
    if direction == 0:
        temp = (positionHistory[snakeLen - 1][0] + add)
        if temp >= width:
            temp -= width
        positionHistory.append((temp, positionHistory[snakeLen - 1][1]))
    elif direction == 1:
        temp = (positionHistory[snakeLen - 1][1] - add)
        if temp < 0:
            temp += height
        positionHistory.append((positionHistory[snakeLen - 1][0],  temp))
    elif direction == 2:
        temp = (positionHistory[snakeLen - 1][0] - add)
        if temp < 0:
            temp += width
        positionHistory.append((temp, positionHistory[snakeLen - 1][1]))
    else:
        temp = (positionHistory[snakeLen - 1][1] + add)
        if temp >= height:
            temp -= height
        positionHistory.append((positionHistory[snakeLen - 1][0], temp))

def CheckGame():
    global total, snakeLen
    if total == snakeLen:
        return True
    return False

def CheckDead(positionArray):
    arrLen = len(positionArray) - 1
    for index, x in enumerate(positionArray):
        if index == arrLen:
            return False
        if x == positionArray[arrLen]:
            return True
    
    return False

# Initialize Game
pygame.init()
pygame.display.set_caption("New Caption")

# Initialize Variable
GREEN = (127,255,0)
BLACK = (0, 0, 0)
HEAD = (32,178,170)
size = 1000, 1000
add = 40
direction = 0 #0 Right, 1 Up, 2 Left, 3 Bottom
width, height = size
startX = width // 2
startY = height // 2
startX -= startX % add
startY -= startY % add

# Total Length to win the game
total = (size[0] // add) * (size[1] // add)

# Food Array
food = []

# Pygame Screen
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.display.update()

# Position History For Snake
positionHistory = [(startX, startY), (startX, startY + add)]
snakeLen = 2

# Draw First 2 Dot
pygame.draw.rect(screen, GREEN, pygame.Rect(positionHistory[0][0], positionHistory[0][1], add, add))
pygame.draw.rect(screen, GREEN, pygame.Rect(positionHistory[1][0], positionHistory[1][1], add, add))

pygame.display.update()

running = True

win = False
# Unlimited Loop
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and direction != 2:
                direction = 0
            elif event.key == K_UP and direction != 3:
                direction = 1
            elif event.key == K_LEFT and direction != 0:
                direction = 2
            elif event.key == K_DOWN and direction != 1:
                direction = 3
    
    if len(food) == 0:
        food.append(GenerateFood())

    PositionAppend(positionHistory, direction)

    flag = 1
    if positionHistory[snakeLen] == food[0]:
        flag = 0
        food.pop()
        snakeLen+=1

    for index, x in enumerate(positionHistory):
        if index == 0 and flag == 1:
            pygame.draw.rect(screen, BLACK, pygame.Rect(x[0], x[1], add, add))
        elif index == snakeLen:
            pygame.draw.rect(screen, HEAD, pygame.Rect(x[0], x[1], add, add))
        else:
            pygame.draw.rect(screen, GREEN, pygame.Rect(x[0], x[1], add, add))
    if flag:
        positionHistory.pop(0)
    
    pygame.display.update()

    if CheckGame():
        win = True
        break

    if CheckDead(positionHistory, ):
        break

    pygame.time.wait(100)

        
if win:
    print("You Win")
else:
    print("Game Over")
    
pygame.quit()


