import random

import pygame
from pygame import Rect


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "(%s,%s,%s)" % (self.r, self.g, self.b)

    @staticmethod
    def random():
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @staticmethod
    def black():
        return Color(0, 0, 0)

    @staticmethod
    def white():
        return Color(255, 255, 255)

    @staticmethod
    def red():
        return Color(255, 0, 0)

    @staticmethod
    def green():
        return Color(0, 255, 0)

    @staticmethod
    def blue():
        return Color(0, 0, 255)

    @staticmethod
    def from_hex(hex_str):
        return list(bytes.fromhex(hex_str))

    def as_tuple(self):
        return self.r, self.g, self.b


class Address:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return "(%s,%s)" % (self.r, self.c)

    def as_tuple(self):
        return self.r, self.c


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)

    def as_tuple(self):
        return self.x, self.y


class Dimensions:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return "(%s,%s)" % (self.r, self.c)

    def as_tuple(self):
        return self.r, self.c


class Cell:
    def __init__(self, address=Address(0, 0)):
        self.surface = None
        self.color = Color.green()
        self.rect = None
        self.border_width = 1
        self.address = address

    def update(self, surface, rect=Rect(0, 0, 0, 0)):
        self.surface = surface
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.surface, self.color.as_tuple(), self.rect, self.border_width)

    def under(self, pos):
        return self.rect.x <= pos.x <= self.rect.x + self.rect.w and self.rect.y <= pos.y <= self.rect.y + self.rect.h


class Grid:
    def __init__(self, surface, rect=Rect(0, 0, 0, 0), dim=Dimensions(0, 0), bg_color=Color.black(),
                 fg_color=Color.white(), margin=0):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.cells = []
        self.rect = rect
        self.dim = dim
        self.margin = margin
        self.prev_cell = None
        for row_n in range(0, self.dim.r):
            arr = []
            for col_n in range(0, self.dim.c):
                cell = Cell(Address(col_n, row_n))
                arr.append(cell)
            self.cells.append(arr)

    def update(self, surface, rect=Rect(0, 0, 0, 0), bg_color=Color.black(),
               fg_color=Color.white(), margin=0):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.rect = rect
        self.margin = margin

        if len(self.cells) > 0:
            for row in self.cells:
                for cell in row:
                    x = cell.address.r * self.rect.w // self.dim.c + self.margin
                    y = cell.address.c * self.rect.h // self.dim.r + self.margin
                    w = self.rect.w // self.dim.c - self.margin * 2
                    h = self.rect.h // self.dim.r - self.margin * 2
                    cell.update(surface, Rect(x, y, w, h))

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color.as_tuple(), self.rect)
        for row in self.cells:
            for cell in row:
                cell.draw()

    def cell_by_pos(self, pos):
        for row in self.cells:
            for cell in row:
                if cell.rect.collidepoint(pos):
                    return cell
        return None
