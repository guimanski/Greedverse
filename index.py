import pygame


pygame.init()

screen = pygame.display.set_mode((960, 780))

# Import assets
warrior_img = pygame.image.load('./assets/test.png').convert_alpha()
warrior_img = pygame.transform.scale(warrior_img, (460, 460))

warriors = pygame.Surface((64, 64), pygame.SRCALPHA)
warriors.blit(warrior_img, (0, 0))
warriors.blit(warrior_img, (20, 0))
warriors.blit(warrior_img, (40, 0))
warriors.blit(warrior_img, (60, 0))


running = True
x = 0
y = 0
clock = pygame.time.Clock()
delta_time = 0.1

while running:
    screen.fill((5, 5, 5))

    screen.blit(warriors, (x, 30))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    
pygame.quit()
