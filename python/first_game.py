import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600))
print(screen)
pygame.display.set_caption("Pygame Tutorial")
clock = pygame.time.Clock()
print(clock)
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
print(player_pos)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Pick the screen color
    screen.fill("silver")

    # Render OUR game here
    pygame.draw.circle(screen, "blue", player_pos, 50)

    # Move our circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
        print(f"plyer goes up by: {player_pos.y}")
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
        print(f"plyer goes down by: {player_pos.y}")
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip the output to display our work on the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
