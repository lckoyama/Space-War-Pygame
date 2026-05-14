import pygame
import random
from nave import Nave
from asteroide import Asteroide
from shot import Shot

pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Space War - TDE")

#fonte 
fonte_titulo = pygame.font.SysFont(None, 50)
fonte_instrucoes = pygame.font.SysFont(None, 30)

objectGroup = pygame.sprite.Group()
asteroideGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#som
background_music = pygame.mixer.music.load("data/fly.mp3")
pygame.mixer.music.set_volume(0.1)
shoot_sound = pygame.mixer.Sound("data/laser shot.wav")

#morte, reiniciar o jogo
def reiniciar_jogo():
    global nave, timer, game_over, game_won, survival_timer
    objectGroup.empty()
    asteroideGroup.empty()
    shotGroup.empty()

    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/space.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    
    nave = Nave(objectGroup)
    timer = 0
    survival_timer = 0 
    game_over = False
    game_won = False   

    pygame.mixer.music.play(-1)

reiniciar_jogo()
gameLoop = True
clock = pygame.time.Clock()

while gameLoop:
    clock.tick(60)
    
    #funções das teclas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        
        if event.type == pygame.KEYDOWN:
            if not game_over and not game_won:
                if event.key == pygame.K_SPACE:
                    shoot_sound.play()
                    Shot(nave.rect.right, nave.rect.centery, objectGroup, shotGroup)
            else:     
                if event.key == pygame.K_r:
                    reiniciar_jogo()
                if event.key == pygame.K_ESCAPE:
                    gameLoop = False

    #logica do meu jogo 
    if not game_over and not game_won:
        objectGroup.update()

        survival_timer += 1
        if survival_timer >= 3400:
            game_won = True
            pygame.mixer.music.stop()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                Asteroide(objectGroup, asteroideGroup)

        #colisão
        pygame.sprite.groupcollide(shotGroup, asteroideGroup, True, True, pygame.sprite.collide_mask)
        
        if pygame.sprite.spritecollide(nave, asteroideGroup, False, pygame.sprite.collide_mask):
            game_over = True 
            pygame.mixer.music.stop()

    #imagem
    if not game_over and not game_won:
        display.fill([46, 46, 46])
        objectGroup.draw(display)
        
    elif game_over:
        display.fill([0, 0, 0])
        texto_morte = fonte_titulo.render("GAME OVER", True, [255, 0, 0])
        texto_retry = fonte_instrucoes.render("Pressione R para Reiniciar ou ESC para Sair", True, [255, 255, 255])
        
        display.blit(texto_morte, [840//2 - texto_morte.get_width()//2, 150])
        display.blit(texto_retry, [840//2 - texto_retry.get_width()//2, 280])
        
    elif game_won:
        display.fill([0, 0, 0])
        texto_vitoria = fonte_titulo.render("VITÓRIA!", True, [0, 255, 0]) # Texto Verde
        texto_retry = fonte_instrucoes.render("Pressione R para Jogar Novamente ou ESC para Sair", True, [200, 200, 200])
        
        display.blit(texto_vitoria, [840//2 - texto_vitoria.get_width()//2, 120])
        display.blit(texto_retry, [840//2 - texto_retry.get_width()//2, 280])

    pygame.display.update()