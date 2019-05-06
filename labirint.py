import pygame
import time
from math import fabs

pygame.init()

#--------------------------
WIDTH = HEIGHT = 20

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.color = (255, 242, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        self.dx = 256
        self.dy = 256
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, WIDTH, HEIGHT)

    def update(self, t, blocks):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dx = -256
        if keys[pygame.K_RIGHT]:
            self.dx = 256
        if keys[pygame.K_UP]:
            self.dy = -256
        if keys[pygame.K_DOWN]:
            self.dy = 256


        self.x += self.dx * t
        self.rect = pygame.Rect(self.x, self.y, WIDTH, HEIGHT)
        self.collide(True, blocks)
        self.dx = 0

        self.y += self.dy * t
        self.rect = pygame.Rect(self.x, self.y, WIDTH, HEIGHT)
        self.collide(False, blocks)
        self.dy = 0

        self.rect = pygame.Rect(self.x, self.y, WIDTH, HEIGHT)
        pygame.draw.rect(window, (190, 42, 78), self.rect)

    def collide(self, bool, blocks):
        for b in blocks:
            if pygame.sprite.collide_rect(self, b):
                if self.dx > 0 and bool: self.x = b.rect.x - WIDTH
                if self.dx < 0 and bool: self.x = b.rect.x + BLOCK_WIDTH

                if self.dy > 0 and not bool: self.y = b.rect.y - HEIGHT
                if self.dy < 0 and not bool: self.y = b.rect.y + BLOCK_HEIGHT

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

#--------------------------

DISPLAY = (872, 632) #розмір вікна
window = pygame.display.set_mode(DISPLAY)

map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1],
       [1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1],
       [1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
       [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
       [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
       [1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
       [1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
       [1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1],
       [1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1],
       [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
       [1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
       [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1]]

BLOCK_WIDTH = BLOCK_HEIGHT = 24

def draw_map(map):
    x = y = 64
    for line in map:
        for el in line:
            if el == 1:
                pygame.draw.rect(window, (255, 242, 0), (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
        x = 64

def text_objects(text, font, color):  # color (R,G,B)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def gameover(totalTime):
    pygame.draw.rect(window, (0, 0, 0), (0, 0, DISPLAY[0], DISPLAY[1]))

    largeText = pygame.font.SysFont("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects("Game over", largeText, (200, 200, 200))
    TextRect.center = ((DISPLAY[0] / 2), (DISPLAY[1] / 2))
    window.blit(TextSurf, TextRect)

    largeText = pygame.font.SysFont("freesansbold.ttf", 30)
    TextSurf, TextRect = text_objects("Total time: " + str(round(totalTime, 3)), largeText, (200, 200, 200))
    TextRect.center = ((DISPLAY[0] / 2), (DISPLAY[1] / 2)+80)
    window.blit(TextSurf, TextRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():  # вихід при нажатії на крест в углу
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def main():
    startX = startY = 0
    finishX = finishY = 0

    blocks = []

    x = y = 64
    for line in map:
        for el in line:
            if el == 1:
                blocks.append(Block(x, y))

            if el == 2:
                startX = x + 2
                startY = y + 2
            if el == 3:
                finishX = x + 2
                finishY = y + 2

            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
        x = 64

    player = Player(startX, startY)
    t = time.time()
    totalTime = 0
    distanceX = player.getX()
    distanceY = player.getY()
    totalDistance = 0

    while True:

        for event in pygame.event.get():  #вихід при нажатії на крест в углу
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.rect(window, (0, 0, 0), (0, 0, DISPLAY[0], DISPLAY[1]))
        draw_map(map)

        TextSurf, TextRect = text_objects("Time: " + str(round(totalTime, 1)), pygame.font.SysFont("freesansbold.ttf", 20), (200, 200, 200))
        TextRect.x = TextRect.y = 32
        window.blit(TextSurf, TextRect)

        t = time.time() - t
        totalTime += t

        player.update(t, blocks)
        totalDistance += fabs(distanceX - player.getX()) + fabs(distanceY - player.getY())

        distanceX = player.getX()
        distanceY = player.getY()

        t = time.time()


        if player.getX() > finishX and player.getY() > finishY:
            gameover(totalTime)

        pygame.display.update()

###-------------------------------------------

main()