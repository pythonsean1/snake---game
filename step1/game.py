import pygame

pygame.init()

# dis is for display
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Sean')

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()