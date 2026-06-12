import pygame
import random
import math

#initialize pygame
        pygame.init()

        #screen settings
        width, height = 600, 900
        screen = pygame.display.set.model((width, height))
        pygame.display.set_caption("Particle Fireworks")

        #color
        Black = (0, 0, 0)

        #----Particle Class ----
        class Particle:
            def_init_(self, x, y, color, vel_x, vel_y, lifetime)
            self.x = x
            self.y = y
            self.color = color