import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/nave.png")
        self.image = pygame.transform.scale(self.image, [100, 100])

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

        # move
        self.speed = 0
        self.acceleration = 0.5 
        self.friction = 0.95  

    def update(self, *args):
        keys = pygame.key.get_pressed()

        # acceleration
        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        else:
            self.speed *= self.friction
        if self.speed > 10:
            self.speed = 10
        elif self.speed < -10:
            self.speed = -10

        # velocidade Y
        self.rect.y += self.speed
        
        # collider
        if self.rect.y < 0:
            self.rect.top = 0
            self.speed = 0 
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0