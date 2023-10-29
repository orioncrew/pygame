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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a=a+1
            elif event.key == pygame.K_d:
                a=a-1
            if event.key == pygame.K_w:
                b=b+1
            elif event.key == pygame.K_s:
                b=b-1
