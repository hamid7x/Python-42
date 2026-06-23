import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Game")
clock = pygame.time.Clock()
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            pos = pygame.mouse.get_pos()
            player_pos.x, player_pos.y = pos
        # elif event.type == pygame.MOUSEMOTION:
        #     pos = pygame.mouse.get_pos()
        #     print(pos)
        #     player_pos.x, player_pos.y = pos
        elif event.type == pygame.MOUSEWHEEL:
            pos = pygame.mouse.get_pos()
            print(pos)
            player_pos.x, player_pos.y = pos
    screen.fill("silver")
    pygame.draw.circle(screen, "blue", player_pos, 40)
    
    # move with keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    pygame.display.flip()

    # move with mouse
 
    dt = clock.tick(60) / 1000

pygame.quit()