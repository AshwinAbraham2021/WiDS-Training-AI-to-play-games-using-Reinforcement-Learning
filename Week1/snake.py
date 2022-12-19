import pygame
from pygame.locals import *

sq_size = 20
move_size = sq_size*1.5

class Square(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Square, self).__init__()
        self.surf = pygame.Surface((sq_size, sq_size))
        self.surf.fill((0, 200, 255))
        # self.rect = self.surf.get_rect()
        self.pos = [x, y]


pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
 
count = 5
square = [Square(40, 40) for _ in range(count)]

dirn = [0]*count

move = {
    0 : [0, move_size],
    1 : [move_size, 0],
    2 : [0, -move_size],
    3 : [-move_size, 0]
}

# Use blit to put something on the screen
screen.blit(square[0].surf, tuple(square[0].pos))

# Update the display using flip
pygame.display.flip()

gameOn = True
# Our game loop
while gameOn:
    # for loop through the event queue
    pygame.time.Clock().tick(60)
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
    keys = pygame.key.get_pressed()

    print(square[0].pos, square[1].pos, dirn[-5:])

    for i in range(count):
        square[i].surf.fill((0, 0, 0))
        screen.blit(square[i].surf, tuple(square[i].pos)) # Remove old square[i]
        square[i].surf.fill((0, 200, 255))

    if keys[K_w] or keys[K_UP]:
        square[0].pos[1] -= move_size
        dirn.append(0)
    elif keys[K_a] or keys[K_LEFT]:
        square[0].pos[0] -= move_size
        dirn.append(1)
    elif keys[K_s] or keys[K_DOWN]:
        square[0].pos[1] += move_size
        dirn.append(2)
    elif keys[K_d] or keys[K_RIGHT]:
        square[0].pos[0] += move_size
        dirn.append(3)

    for i in range(1, count):
        square[i].pos = [square[i-1].pos[j] + move[dirn[-i]][j] for j in [0, 1]]

    for i in range(count):
        square[i].pos[0] %= W
        square[i].pos[1] %= H
        screen.blit(square[i].surf, tuple(square[i].pos)) # Put new square[i]
    
    # Update the display using flip
    pygame.display.flip()

pygame.quit()