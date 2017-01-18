import pygame
from pygame import Rect


class Cell:
    def __init__(self, surface, color, x_pos, y_pos, width, height, r_c=(0, 0), border_width=1):
        self.surface = surface
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.border_width = border_width
        self.r_c = r_c

    def draw(self):
        pygame.draw.rect(self.surface, self.color, Rect(self.x_pos, self.y_pos, self.width, self.height),
                         self.border_width)

    def under(self, pos):
        return self.x_pos <= pos[0] <= self.x_pos + self.width and self.y_pos <= pos[1] <= self.y_pos + self.height


class Grid:
    def __init__(self, surface, x_pos, y_pos, row_cnt, col_cnt, width, height, bg_color=(0, 0, 0),
                 fg_color=(255, 255, 255), margin=1):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.cells = []
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_cnt = row_cnt
        self.col_cnt = col_cnt
        self.width = width
        self.height = height
        self.margin = margin
        self.prev_cell = None
        for row_n in range(0, self.row_cnt):
            arr = []
            for col_n in range(0, self.col_cnt):
                x = col_n * self.width // self.col_cnt + self.margin
                y = row_n * self.height // self.row_cnt + self.margin
                w = self.width // self.col_cnt - self.margin * 2
                h = self.height // self.row_cnt - self.margin * 2
                cell = Cell(self.surface, self.fg_color, x, y, w, h, (col_n, row_n))
                arr.append(cell)
            self.cells.append(arr)

    def update(self, surface, x_pos, y_pos, row_cnt, col_cnt, width, height, bg_color=(0, 0, 0),
               fg_color=(255, 255, 255), margin=1):
        self.surface = surface
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_cnt = row_cnt
        self.col_cnt = col_cnt
        self.width = width
        self.height = height
        self.margin = margin

        if len(self.cells) > 0:
            for row in self.cells:
                for cell in row:
                    cell.x_pos = cell.r_c[0] * self.width // self.col_cnt + self.margin
                    cell.y_pos = cell.r_c[1] * self.height // self.row_cnt + self.margin
                    cell.width = self.width // self.col_cnt - self.margin * 2
                    cell.height = self.height // self.row_cnt - self.margin * 2

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, Rect(self.x_pos, self.y_pos, self.width, self.height))
        for row in self.cells:
            for cell in row:
                cell.draw()

    def cell_by_pos(self, pos):
        for row in self.cells:
            for cell in row:
                if cell.under(pos):
                    return cell
        return None
