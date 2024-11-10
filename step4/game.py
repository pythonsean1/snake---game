import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

# This is the game over colour
red = (255, 0, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Sean')

game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

# size of snake block
snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
# sets the speed of the snake block
snake_speed = 20

# sets the font of the game over text
font_style = pygame.font.SysFont(None, 50)

# message function that displays text in the game - game over text
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    # we are displaying the message back to the game
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

while not game_over:
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

    # if snake hits the border game is over
    # only one of the 4 conditions need to be true
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

    pygame.display.update()

    # Contorls the movement on how fast the snake is moving
    clock.tick(snake_speed)

# Displays the gave over message back to the user
message("You lost!", red)
# updates the display screen with the game over message
pygame.display.update()
# sets the timer to 2 seconds to automatically shut down
time.sleep(2)

# Quits the game automatically()
pygame.quit()
quit()