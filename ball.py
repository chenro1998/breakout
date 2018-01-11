import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.speedx = 5
        self.speedy = 3
        self.sound = pygame.mixer.Sound('bricks.wav')

    def move(self):
        self.rect.right += self.speedx
        self.rect.bottom += self.speedy

        if self.rect.right >= self.windowWidth or self.rect.left <= 0:
            print(self.speedx)
            self.speedx = -self.speedx
        if self.rect.top > self.windowHeight or self.rect.bottom < 0:
            self.speedy = -self.speedy

    def collide_bricks(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.sound.play()

            self.speedy = -self.speedy
            return True
        else:
            return False

    def collide_paddle(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.sound.play()
            self.speedy = -self.speedy