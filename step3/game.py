import pygame

pygame.init()

# colour of the background
white = (255, 255, 255)
# colour of the snake
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Sean')

game_over = False

# this sets the position of the snake
x1 = 300
y1 = 300

# This contols the movement of the snake
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # this controls the movement via the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    # This updates the movement of the snake when the user enters up, down, left, or right buttons
    x1 += x1_change
    y1 += y1_change

    # create the white background for the game
    dis.fill(white)

    # the snake is black
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()