import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

# bloco de variáveis
white = (255, 255, 255)
running = True
rect_width = 100
rect_height = 50
rect_speed = 7
floor = 500
on_the_floor = False
gravity = 0.8
jump_strength = -20
rect_y_speed = 0

rectangle = pygame.Rect(0, 100, rect_width, rect_height) #esquerda, topo, largura e altura

while running:

    screen.fill((5, 5, 5))

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if on_the_floor:
                rect_y_speed = jump_strength
                on_the_floor = False

            



    keys = pygame.key.get_pressed()
    
    # --- BLOCO DE MOVIMENTAÇÃO --- #
    if  keys[pygame.K_d]:
        rectangle.x += rect_speed

    if keys[pygame.K_a]:
        rectangle.x -= rect_speed

    # sistema de gravidade
    rect_y_speed += gravity
    rectangle.y += rect_y_speed


    # --- BLOCO DE CORREÇÃO --- #
    on_the_floor = False

    if rectangle.left < 0:
        rectangle.left = 0

    if rectangle.right > 800:
        rectangle.right = 800

    if rectangle.bottom >= floor:
        rectangle.bottom = floor
        rect_y_speed = 0
        on_the_floor = True
    

    pygame.draw.rect(screen, white, rectangle) # desenha o retângulo em screen - surface, cor, objeto


    pygame.display.flip()   
    clock.tick(60)

pygame.quit()
