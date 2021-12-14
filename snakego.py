import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#1.显示界面设置
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#2.时钟设置
clock = pygame.time.Clock()

#3.其他设置
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#4.蛇的设置：
snake_block = 10
snake_speed = 15 
#pygame.draw.rect是绘制矩形的意思，第一个参数：绘制在哪里；第二个参数：绘制线条的颜色；第三个参数：位置 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
#5.蛇的运动设置 
def gameLoop(): #因为蛇捕食食物是一个周而复始的过程，所以我们先构建一个循环函数
    game_over = False #游戏正常运行我们认为是True，如果游戏结束和游戏终止都是False
    game_close = False
 
    #x和y来确定蛇的初始位置，x1和y1change来记录蛇的位置变化
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
 
    #蛇的长度就是蛇头
    snake_List = []
    Length_of_snake = 1
 
#8.设置食物位置 round函数是四舍五入后的结果
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
#6.当游戏终止时，界面显示xxxx，且此时你的分数是蛇长度-1.
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
#当发现时，界面显示xxxx，且此时你的分数是蛇长度-1. keydown是pygame用来实现移动的功能。在这里使用pygame的函数，添加快捷键方式。
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
#7.蛇运动终止                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
#9.蛇吃一个食物，身体增加一截      用列表的方式  
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

gameLoop()