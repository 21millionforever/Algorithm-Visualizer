import pygame
from sys import exit
from cell import *
from messages import *

SCREEN_HEIGHT, SCREEN_WIDTH = 700, 1300
CELL_HEIGHT, CELL_WIDTH = 20, 20
HEIGHT_PAD, SIDE_PAD = 200, 200
CELL_COLOR = (0, 100, 255)

def main():

    # Initialize pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Starting point surface
    starting_point_surf = None

    # End point surface
    end_point_surf = None

    # Text font
    # text_font = pygame.font.SysFont('Normal text', 50)

    # Visualizer status
    is_choosing_s_point = True
    is_choosing_e_point = False

    # Create cells
    cells = CreateCells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_HEIGHT, CELL_WIDTH, HEIGHT_PAD, SIDE_PAD)
    while True:
        # Background
        screen.fill('White')
        # Drawing cells
        DrawCells(cells, screen, CELL_COLOR)

        # Handle different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Place starting and end point
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Draw the starting point
                # if is_choosing_s_point and event.pos[0] > SIDE_PAD // 2 and \
                #    event.pos[0] < SCREEN_WIDTH - SIDE_PAD // 2 and \
                #    event.pos[1] > HEIGHT_PAD // 2 and \
                #    event.pos[1] < SCREEN_HEIGHT - HEIGHT_PAD // 2:

                if is_choosing_s_point and isPosWithinCells(event.pos[0], event.pos[1], SCREEN_HEIGHT, SCREEN_WIDTH, SIDE_PAD, HEIGHT_PAD):
                    pos_x, pos_y = event.pos[0], event.pos[1]
                    # s_row, s_col = getRowAndCol(pos_x, pos_y, SIDE_PAD, HEIGHT_PAD, CELL_WIDTH, CELL_HEIGHT)
                    s_row, s_col = int((pos_y - HEIGHT_PAD / 2) / CELL_HEIGHT), int((pos_x - SIDE_PAD / 2) / CELL_WIDTH)
                    starting_point_surf = cells[s_row][s_col].cell_surf
                    starting_point_surf.fill('Red')

                # Draw the end point
                if is_choosing_e_point and event.pos[0] > SIDE_PAD // 2 and \
                   event.pos[0] < SCREEN_WIDTH - SIDE_PAD // 2 and \
                   event.pos[1] > HEIGHT_PAD // 2 and \
                   event.pos[1] < SCREEN_HEIGHT - HEIGHT_PAD // 2:
                    pos_x, pos_y = event.pos[0], event.pos[1]
                    e_row, e_col = int((pos_y - HEIGHT_PAD / 2) / CELL_HEIGHT), int((pos_x - SIDE_PAD / 2) / CELL_WIDTH)
                    end_point_surf = cells[e_row][e_col].cell_surf
                    end_point_surf.fill('Blue')




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_choosing_s_point = False
                    is_choosing_e_point = True

        # Draw the starting point
        if starting_point_surf is not None:
            screen.blit(starting_point_surf,(cells[s_row][s_col].pos_x, cells[s_row][s_col].pos_y))
        # # Draw the messages when the user is choosing the starting point
        if is_choosing_s_point:
            drawTextOnStartingPointScreen(screen)

        # Draw the message when the user is choosing the end point
        if end_point_surf is not None:
            screen.blit(end_point_surf, (cells[e_row][e_col].pos_x, cells[e_row][e_col].pos_y))
        if is_choosing_e_point:
            drawTextOnEndPointScreen(screen)












        clock.tick(60)
        pygame.display.update()



if __name__ == "__main__":
    main()

