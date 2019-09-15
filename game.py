import pygame
import time
import random
import sys

from settings import Settings


class Foot:
    def __init__(self, side):
        image = pygame.image.load(f'images/flat-white-{side}.png')
        self.image = pygame.transform.scale(image, Settings.image_size)

        self.rect = self.image.get_rect()
        self.rect.move_ip(int(Settings.width / 2), int(Settings.height / 2))

    def move(self, direction, distance):
        dx, dy = {'up': (0, -1), 'left': (-1, 0), 'right': (1, 0), 'down': (0, 1)}[direction]
        distance = Settings.multiplier * float(distance)
        self.rect.move_ip(dx * distance, dy * distance)

    def draw(self, canvas):
        canvas.blit(self.image, self.rect)


class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.feet = {f: Foot(f) for f in ['l', 'r']}
        self.feet['r'].rect.move_ip(50, 0)

    def draw(self):
        canvas.fill(Settings.background_colour)
        for foot in self.feet.values():
            foot.draw(self.canvas)
        pygame.display.flip()


with open('dance.txt') as input_file:
    dance = input_file.readlines()

canvas = pygame.display.set_mode((Settings.width, Settings.height))
game = Game(canvas)

while True:
    for line in dance:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        game.draw()
        time.sleep(Settings.delay)

        for part in line.split(','):
            foot, direction, distance = [p.strip() for p in part.split()]
            distance = float(distance)
            game.feet[foot].move(direction, distance)

    random.shuffle(dance)
