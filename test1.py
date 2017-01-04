import pygame
from pygame import Rect


class Cell:
    def __init__(self, surface, color, x, y, w, h):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = 0

    def draw(self):
        pygame.draw.rect(self.surface, self.color, Rect(self.x, self.y, self.w, self.h))


class Grid:
    def __init__(self, surface, bg_color, fg_color, x, y, r, c, w, h, m=1):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.cells = []
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.w = w
        self.h = h
        self.m = m
        self.create()

    def create(self):
        if len(self.cells) > 0:
            for r in self.cells:
                for c in r:
                    c.x = self.c.id[0] * self.w // self.c + self.m
                    c.y = self.c.id[1] * self.h // self.r + self.m
                    c.w = self.w // self.c - self.m * 2
                    c.h = self.h // self.r - self.m * 2
        else:
            print('init')
            for r in range(0, self.r):
                row = []
                for c in range(0, self.c):
                    x = c * self.w // self.c + self.m
                    y = r * self.h // self.r + self.m
                    w = self.w // self.c - self.m * 2
                    h = self.h // self.r - self.m * 2
                    cell = Cell(self.surface, self.fg_color, x, y, w, h)
                    cell.id = (c, r)
                    row.append(cell)
                self.cells.append(row)

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, Rect(self.x, self.y, self.w, self.h))
        for r in self.cells:
            for c in r:
                c.draw()

    def cell_by_pos(self, pos):
        for r in self.cells:
            for c in r:
                if c.x <= pos[0] <= c.x + c.w and c.y <= pos[1] <= c.y + c.h:
                    return c
        return None
