import pygame

pygame.init()

DISPLAY = (800, 600) #розмір вікна
window = pygame.display.set_mode(DISPLAY)

map = [[1, 3, 2, 3, 3, 3, 0, 2, 3, 3, 3, 3, 2],
       [6, 4, 8, 0, 3, 3, 2, 5, 0, 1, 3, 2, 5],
       [7, 4, 5, 4, 4, 4, 5, 8, 0, 6, 5, 5, 5],
       [6, 5, 0, 0, 6, 0, 0, 0, 0, 0, 5, 5, 5],
       [6, 3, 3, 0, 6, 3, 2, 3, 3, 3, 3, 5, 5],
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]]

blocks = ['elements/bl1.png', 'elements/bl2.png', 'elements/bl3.png', 'elements/bl4.png',
          'elements/bl5.png', 'elements/bl6.png', 'elements/bl7.png', 'elements/bl8.png']

BLOCK_WIDTH = BLOCK_HEIGHT = 32

while True:
    for event in pygame.event.get():  #вихід при нажатії на крест в углу
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = y = 64
    for line in map:
        for el in line:
            if el == 1:
                block = pygame.image.load(blocks[0])  #закідуєм картінку у змінну
                window.blit(block, (x, y))            #прорисовуєм у нужних коордінатах

            if el == 2:
                block = pygame.image.load(blocks[1])
                window.blit(block, (x, y))

            if el == 3:
                block = pygame.image.load(blocks[2])
                window.blit(block, (x, y))

            if el == 4:
                block = pygame.image.load(blocks[3])
                window.blit(block, (x, y))

            if el == 5:
                block = pygame.image.load(blocks[4])
                window.blit(block, (x, y))

            if el == 6:
                block = pygame.image.load(blocks[5])
                window.blit(block, (x, y))

            if el == 7:
                block = pygame.image.load(blocks[6])
                window.blit(block, (x, y))

            if el == 8:
                block = pygame.image.load(blocks[7])
                window.blit(block, (x, y))

            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
        x = 64

    pygame.display.update()