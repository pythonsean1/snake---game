import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake game by Sean')

# set the colours for the snake and the food
blue = (0,0,255)
red = (255,0,0)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    
    # draw function to create a rectange(this will be our snake)
    pygame.draw.rect(dis,blue,[200,150,10,10])

    # This updates any changes that you have made
    pygame.display.update()

pygame.quit()
quit()