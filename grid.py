import pygame
import random
from pygame import Rect


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "(%s,%s,%s)" % (self.r, self.g, self.b)

    def set_random(self):
        self.r, self.g, self.b = Color.random()

    @staticmethod
    def random():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    @staticmethod
    def black():
        return 0, 0, 0

    @staticmethod
    def white():
        return 255, 255, 255

    @staticmethod
    def red():
        return 255, 0, 0

    @staticmethod
    def green():
        return 0, 255, 0

    @staticmethod
    def blue():
        return 0, 0, 255

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
    def __init__(self, surface, color=Color.black(), rect=Rect(0, 0, 0, 0), address=Address(0, 0),
                 border_width=1):
        self.surface = surface
        self.color = color
        self.rect = rect
        self.border_width = border_width
        self.address = address

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect, self.border_width)

    def under(self, pos):
        return self.rect.x <= pos.x <= self.rect.x + self.rect.w and self.rect.y <= pos.y <= self.rect.y + self.rect.h


class Grid:
    def __init__(self, surface, rect=Rect(0, 0, 0, 0), dim=Dimensions(0, 0), bg_color=Color.black(),
                 fg_color=Color.white(), margin=1):
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
                x = col_n * self.rect.w // self.dim.c + self.margin
                y = row_n * self.rect.h // self.dim.r + self.margin
                w = self.rect.w // self.dim.c - self.margin * 2
                h = self.rect.h // self.dim.r - self.margin * 2
                cell = Cell(self.surface, self.fg_color, Rect(x, y, w, h), Address(col_n, row_n))
                arr.append(cell)
            self.cells.append(arr)

    def update(self, surface, rect=Rect(0, 0, 0, 0), dim=Dimensions(0, 0), bg_color=Color.black(),
               fg_color=Color.white(), margin=1):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.rect = rect
        self.dim = dim
        self.margin = margin

        if len(self.cells) > 0:
            for row in self.cells:
                for cell in row:
                    cell.rect.x = cell.address.r * self.rect.w // self.dim.c + self.margin
                    cell.rect.y = cell.address.c * self.rect.h // self.dim.r + self.margin
                    cell.rect.w = self.rect.w // self.dim.c - self.margin * 2
                    cell.rect.h = self.rect.h // self.dim.r - self.margin * 2

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
        for row in self.cells:
            for cell in row:
                cell.draw()

    # def cell_by_pos(self, pos):
    #     for row in self.cells:
    #         for cell in row:
    #             if cell.under(pos):
    #                 return cell
    #     return None
    def cell_by_pos(self, pos):
        for row in self.cells:
            for cell in row:
                if cell.rect.collidepoint(pos):
                    return cell
        return None
