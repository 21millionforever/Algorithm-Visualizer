import pygame


class Cell:
    def __init__(self, left=None, right=None, top=None, bottom=None, pos_x=0, pos_y=0):
        self.left, self.right = left, right
        self.top, self.bottom = top, bottom
        self.pos_x, self.pos_y = pos_x, pos_y

def CreateCells(screen_height, screen_width, cell_height, cell_width, height_pad, side_pad):
    cells = list()
    for row in range((screen_height - height_pad) // cell_height):
        temp = list()
        for col in range((screen_width - side_pad) // cell_width):
            pos_x, pos_y = col * cell_width, row * cell_height
            c = pygame.Rect(side_pad // 2, height_pad // 2, pos_x, pos_y)
            temp.append(c)
        cells.append(temp)
    return cells
def DrawCells(cells, screen, cell_color):
    for row in cells:
        for cell in row:
            pygame.draw.rect(screen, cell_color, cell, 1)