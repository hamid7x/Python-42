import pygame


pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw Shapes")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("silver")

    # draw a line
    pygame.draw.line(screen, "black", (50, 50), (750, 50), 20)

    # draw a circle
    pygame.draw.circle(screen, "black", (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 100, 10)

    # draw a rectangle
    pygame.draw.rect(screen, "blue", (600, 400, 100, 50))
    pygame.display.flip()


pygame.quit()
