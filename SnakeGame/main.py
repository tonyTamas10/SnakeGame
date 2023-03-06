import pygame
import random

pygame.init()

display_height = 400
display_width = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption("Snake game by Tony")

color = (0, 0, 0)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('aldin', 20)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, 'black', [x[0], x[1], snake_block, snake_block])


def message(msg):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_height/3])


def game_loop():
    game_over = False
    game_closed = False

    snake_block = 10
    snake_speed = 10

    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0)*10.0

    snake_list = []
    snake_lenght = 1

    while not game_over:

        while game_closed is True:
            display.fill('white')
            message("You lost! Press Q to quit or R to play again")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_closed = False
                    elif event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

            if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
                game_closed = True

            x1 += x1_change
            y1 += y1_change

            display.fill('white')

            pygame.draw.rect(display, color, [foodx, foody, snake_block, snake_block])

            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > snake_lenght:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_closed = True

            our_snake(snake_block, snake_list)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
                snake_lenght += 1

            clock.tick(60)

    pygame.quit()
    quit()


game_loop()
