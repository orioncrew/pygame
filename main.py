import pygame

pygame.init()
screen = pygame.display.set_mode((600, 375))
pygame.display.set_caption("abc")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("images/backfon.jpg")

#Test

running = True
a, b =0, 0
while running:


    screen.blit(bg, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
