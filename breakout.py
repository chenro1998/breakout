# Kevin Chen
# 02/11/18
# This program make a breakout pygame


import pygame
import sys
import brick
import paddle
import ball
from pygame.locals import *


def main():
    pygame.init()
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    NUM_TURNS = 3
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    life = 3
    score = 0

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    mainSurface.fill(BLACK)
    xposition = 0
    yposition = BRICK_Y_OFFSET
    color_list = [RED, ORANGE, YELLOW, GREEN, CYAN]
    bricks_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()

    for new_color in color_list:
        for x in range(2):
            for x in range(BRICKS_PER_ROW):
                myBricks = brick.Brick(BRICK_WIDTH, new_color)
                bricks_group.add(myBricks)

                myBricks.rect.x = xposition
                myBricks.rect.y = yposition
                mainSurface.blit(myBricks.image, myBricks.rect)
                xposition += BRICK_WIDTH + BRICK_SEP
            xposition = 0
            yposition += BRICK_HEIGHT + BRICK_SEP

    myPaddle = paddle.Paddle(WHITE)
    paddle_group = pygame.sprite.Group()
    paddle_group.add(myPaddle)
    myPaddle.rect.x = APPLICATION_WIDTH/2
    myPaddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(myPaddle.image, myPaddle.rect)
    myBall = ball.Ball(WHITE, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    myBall.rect.x = APPLICATION_WIDTH/2
    myBall.rect.y = APPLICATION_HEIGHT/2
    ball_group.add(myBall)
    changed_speed = False

    while True:
        if life == 0:
            mainSurface.fill((0, 0, 0))
            font = pygame.font.SysFont("comicsansms", 100)
            text = font.render("Game Over", True, (255, 0, 0))
            mainSurface.blit(text, (10, 300))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit

        elif score == 850:
            mainSurface.fill((0, 0, 0))
            font = pygame.font.SysFont("comicsansms", 100)
            text = font.render("You Win", True, (255, 0, 0))
            mainSurface.blit(text, (10, 300))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit

        elif score == 10 and changed_speed is False:
            myBall.speedx -= 1
            myBall.speedy -= 1
            changed_speed = True

        elif score == 450 and changed_speed is True:
            myBall.speedx -= 1
            myBall.speedy -= 1
            changed_speed = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
        mainSurface.fill(BLACK)
        myPaddle.move(pygame.mouse.get_pos())
        mainSurface.blit(myPaddle.image, myPaddle.rect)
        for bricks in bricks_group:
            mainSurface.blit(bricks.image, bricks.rect)

        myBall.move()
        mainSurface.blit(myBall.image, myBall.rect)

        myBall.collide_paddle(paddle_group)
        if myBall.collide_bricks(bricks_group):
            score += 10

        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render("Score:"+str(score), True, (255, 0, 0))
        mainSurface.blit(text, (220, 20))

        if myBall.rect.bottom > APPLICATION_HEIGHT:
            myBall.rect.x = APPLICATION_WIDTH / 2
            myBall.rect.y = APPLICATION_HEIGHT / 2
            life -= 1

        pygame.display.update()


main()
