import pygame
from pygame import mixer, key
from random import randint


pygame.init()
mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 500))
mixer.music.load('space.ogg')


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, w, h):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        self.speed = 5

    def update(self):
        keys = key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x <= 640:
            self.rect.x += self.speed

    def fire(self):
        pass


class Enemy(GameSprite):
    def __init__(self, image_path, x, y, w, h):
        super().__init__(image_path, x, y, w, h)
        self.speed = 3
    
    def update(self):
        self.rect.y += self.speed


bg = GameSprite('galaxy.jpg', 0, 0, 700, 500)
player = Player('rocket.png', 325, 400, 60, 90)
enemies = pygame.sprite.Group()
for i in range(5):
    x = randint(0, 700)
    y = randint(0, 200)
    enemy = Enemy('ufo.png', x, y, 100, 70)
    enemies.add(enemy)
    
run = True
mixer.music.play()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    bg.draw()
    player.update()
    enemies.update()
    enemies.draw(screen)
    player.draw()
    pygame.display.update()
    clock.tick(30)
