import pygame


class Cell:
    def __init__(self):
        self.left, self.right = None, None
        self.top, self.bottom = None, None
        self.row, self.col = None, None      # 0-indexed
        self.pos_x, self.pos_y = None, None
        self.cell_surf, self.cell_surf_rect, self.cell_rect = None, None, None

def CreateCells(screen_height, screen_width, cell_height, cell_width, height_pad, side_pad):
    cells = list()
    for row in range((screen_height - height_pad) // cell_height):
        temp = list()
        for col in range((screen_width - side_pad) // cell_width):
            pos_x, pos_y = col * cell_width, row * cell_height

            # cell_rect = pygame.Rect(side_pad // 2 + pos_x, height_pad // 2 + pos_y, 20, 20)
            cell_surf = pygame.Surface((20,20))
            cell_surf_rect = cell_surf.get_rect(topleft = (side_pad // 2 + pos_x, height_pad // 2 + pos_y))

            c = Cell()
            c.pos_x, c.pos_y = pos_x + side_pad // 2, pos_y + height_pad // 2

            c.row, c.col = row, col
            # c.cell_rect = cell_rect
            c.cell_surf, c.cell_surf_rect =  cell_surf, cell_surf_rect
            temp.append(c)

        cells.append(temp)
    return cells

def DrawCells(cells, screen, cell_color):
    for row in cells:
        for cell in row:
            pygame.draw.rect(screen, cell_color, cell.cell_surf_rect, 1)

def isPosWithinCells(x,y, screen_height, screen_width, side_pad, height_pad):
    if x > side_pad // 2 and \
        x < screen_width - side_pad // 2 and \
        y > height_pad // 2 and \
        y < screen_height - height_pad // 2:
        return True
    else:
        return False

def getRowAndCol(pos_x, pos_y, size_pad, height_pad, cell_width, cell_height):
    s_row, s_col = int((pos_y - height_pad / 2) / cell_height), int((pos_x - size_pad / 2) / cell_width)
    return (s_row, s_col)


# 25 Rows
# (700 - 200) // 20 = 25