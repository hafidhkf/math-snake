import pygame
import random

particles = []

def add_particles(x, y, color):
    for _ in range(10):
        particles.append([[x, y], [random.uniform(-1, 1), random.uniform(-1, 1)], random.randint(3, 6), color])

def update_particles(screen):
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        if particle[2] > 0:
            pygame.draw.circle(screen, particle[3], (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        else:
            particles.remove(particle)
