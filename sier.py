import pygame
 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
 
pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill( (0,0,0) )
 
for y in range (0, SCREEN_HEIGHT):
    for x in range (0, SCREEN_WIDTH):
        if x & y:
            screen.set_at((x, y), (132,22,23) )
pygame.display.update()
 
while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
