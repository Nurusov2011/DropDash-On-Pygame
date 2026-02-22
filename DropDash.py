import pygame
from sys import exit
from random import randint

def player_animation():
    global player_index, player_surf
    player_index += 0.25
    if player_index >= len(player_walk):
        player_index = 0
    player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((400,800))
pygame.display.set_caption("DropDash")
pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
score = 0
sky= pygame.image.load("sky2.png").convert()
ground = pygame.image.load("grass.png").convert()
ground_rect = ground.get_rect(topleft=(0,650))
apple = pygame.image.load("apple.png").convert_alpha()
apple_rect = apple.get_rect(topleft=(200,0))
player_walk1 = pygame.image.load("player.png").convert_alpha()
player_walk2 = pygame.image.load("player2.png").convert_alpha() 
player_walk = [player_walk1,player_walk2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(200,675))
text_surface2 = font.render(f"Score: {score}", True, (245, 245, 245))
text_surface2_rect = text_surface2.get_rect(topleft=(10,10))
sound = pygame.mixer.Sound("collect.wav")
sound2 = pygame.mixer.Sound("lose.mp3")
game_active = True
facing_left = True
 

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            game_active = True
            score = 0
            text_surface2 = font.render(f"Score: {score}", True, (245, 245, 245))
            apple_rect.left = randint(0,350)
            apple_rect.bottom = 0
    screen.blit(sky,(0,0))
    if game_active:
        screen.blit(apple,apple_rect)
        apple_rect.bottom += 11
        if apple_rect.top > 650:
            apple_rect.left = randint(0,350)
            apple_rect.bottom = 0
        screen.blit(ground,(0,650))
        screen.blit(player_surf,player_rect)
        screen.blit(text_surface2,text_surface2_rect)
        keys = pygame.key.get_pressed()

        if player_rect.colliderect(apple_rect):
            apple_rect.left = randint(0,350)
            apple_rect.bottom = 0
            score += 1
            text_surface2 = font.render(f"Score: {score}", True, (245, 245, 245))  
            sound.play()      

        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.left -= 5
            player_animation()
            facing_left = True
        if keys[pygame.K_RIGHT] and player_rect.right < 400:
            player_rect.right += 5
            player_animation()
            facing_left = False
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            player_index = 0
            player_surf = player_walk[player_index]
        
        if apple_rect.colliderect(ground_rect):
            sound2.play()
            game_active = False
        
        if not facing_left:
            player_surf = pygame.transform.flip(player_surf, True, False)
        else:
            player_surf = pygame.transform.flip(player_surf, False, False)

        
    else:
        pygame.time.wait(1000)
        game_over_surface = font.render("Game Over", True, (255,255,255))
        game_over_surface2 = font.render(f"Final Score: {score}", True, (255,255,255))
        game_over_surface3 = font.render("Press Space to Restart", True, (255,255,255))
        game_over_rect = game_over_surface.get_rect(center=(200,300))
        game_over_rect2 = game_over_surface2.get_rect(center=(200,350))
        game_over_rect3 = game_over_surface3.get_rect(center=(200,400))
        screen.blit(game_over_surface,game_over_rect)
        screen.blit(game_over_surface2,game_over_rect2)
        screen.blit(game_over_surface3,game_over_rect3)
    pygame.display.update()
    clock.tick(60)
