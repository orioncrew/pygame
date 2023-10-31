import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 375))
pygame.display.set_caption("abc")
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)
bg = pygame.image.load("images/backfon.jpg").convert_alpha()
ghost = pygame.image.load("images/ghost.png").convert_alpha()
ghost_list_in_game = []
player = pygame.image.load("images/player_left/tile000.png").convert_alpha()
walk_left = [
    pygame.image.load("images/player_left/tile000.png").convert_alpha(),
    pygame.image.load("images/player_left/tile001.png").convert_alpha(),
    pygame.image.load("images/player_left/tile002.png").convert_alpha(),
    pygame.image.load("images/player_left/tile003.png").convert_alpha(),
    pygame.image.load("images/player_left/tile004.png").convert_alpha(),
    pygame.image.load("images/player_left/tile005.png").convert_alpha()
]

walk_right = [
    pygame.image.load("images/player_right/tile000.png").convert_alpha(),
    pygame.image.load("images/player_right/tile001.png").convert_alpha(),
    pygame.image.load("images/player_right/tile002.png").convert_alpha(),
    pygame.image.load("images/player_right/tile003.png").convert_alpha(),
    pygame.image.load("images/player_right/tile004.png").convert_alpha(),
    pygame.image.load("images/player_right/tile005.png").convert_alpha()
]
bg_x = 0
player_anim_count = 0
player_speed = 5
player_x = 150
player_y = 250

lable = pygame.font.Font("fonts/Roboto-Regular.ttf", 40)
lose_lable = lable.render("Вы проиграли!", False, (193, 196, 199))
restart_lable = lable.render("Играть заново", False, (115, 132, 148))
restart_lable_rect = restart_lable.get_rect(topleft=(180,200))

is_jump = False
jump_count = 7

#bg_sound = pygame.mixer.Sound("sounds/bg.mp3")
#bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)

gameplay = True

running = True
a, b =0, 0
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))

    if gameplay:

        player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -=10

                if el.x < -10:
                    ghost_list_in_game.pop(i)


                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -=1
            else:
                is_jump = False
                jump_count = 7

    # test
        #2222
        if player_anim_count == 5:
            player_anim_count = 0
        else:
            player_anim_count += 1
        bg_x -= 2
        if bg_x <=-600:
            bg_x=0
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_lable, (180, 100))
        screen.blit(restart_lable, restart_lable_rect)

        mouse = pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft = (602, 270)))

    clock.tick(10)