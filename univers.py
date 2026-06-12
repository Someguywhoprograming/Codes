import pygame
import random
import math
import sys

pygame.init()
W, H = 800, 800
S = pygame.display.set_mode((W, H))
C = pygame.time.Clock()  # javítva
BLACK, WHITE = (0, 0, 0), (255, 255, 255)

class Star:
    def __init__(self):
        self.r = random.uniform(0, W//2)
        self.a = random.uniform(0, 2*math.pi)
        self.rs = random.uniform(0.002, 0.006)
        self.ar = random.uniform(0.002, 0.006)
        self.sz = random.uniform(1, 2)

    def move(self):
        self.a += self.ar
        self.r += self.rs
        if self.r > W//2:
            self.r = 0
            self.a = random.uniform(0, 2*math.pi)

    def draw(self):
        x = W//2 + math.cos(self.a) * self.r
        y = H//2 + math.sin(self.a) * self.r
        pygame.draw.circle(S, WHITE, (int(x), int(y)), int(self.sz))  # javítva

stars = [Star() for _ in range(500)]

while True:
    S.fill(BLACK)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for star in stars:
        star.move()
        star.draw()
    pygame.display.flip()
    C.tick(60)