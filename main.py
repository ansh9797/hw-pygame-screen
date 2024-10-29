import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('My first game screen')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, ((640-200)//2, (480-100)//2, 200, 100))


    text = font.render('Hello World', True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=(640//2, 480//2)))

    pygame.display.flip()


pygame.quit()
