import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
white = (255, 255, 255)

running = True
rect_width = 100
rect_height = 50
rect_speed = 7

rectangle = pygame.Rect(0, 100, rect_width, rect_height) #esquerda, topo, largura e altura

while running:

    screen.fill((5, 5, 5))

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    
    # bloco de movimentação
    if  keys[pygame.K_d]:
        rectangle.x += rect_speed

    if keys[pygame.K_a]:
        rectangle.x -= rect_speed

    # bloco de correção
    if rectangle.left < 0:
        rectangle.left = 0

    if rectangle.right > 800:
        rectangle.right = 800
    

    pygame.draw.rect(screen, white, rectangle)    


    pygame.display.flip()   
    clock.tick(60)

pygame.quit()
