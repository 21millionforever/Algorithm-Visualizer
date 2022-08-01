from collections import deque
# import pygame
from sys import exit
from cell import *
from messages import *
import sys
SCREEN_HEIGHT, SCREEN_WIDTH = 700, 1300
CELL_HEIGHT, CELL_WIDTH = 20, 20
HEIGHT_PAD, SIDE_PAD = 200, 200
CELL_COLOR = (0, 100, 255)
ROWS, COLS = 0, 0
sys.setrecursionlimit(2000)
def DFS(curr_cell, end_cell, visited, screen, isFirst = True):
    # Base case
    if curr_cell is None or (curr_cell.row, curr_cell.col) in visited:
        return False
    if curr_cell == end_cell:
        return True

    # Mark we have visited the cell
    visited.add((curr_cell.row, curr_cell.col))
    if not isFirst:
        curr_cell.cell_surf.fill('Pink')
    isFirst = False
    screen.blit(curr_cell.cell_surf, curr_cell.cell_surf_rect)
    pygame.display.update()
    pygame.time.delay(20)

    return DFS(curr_cell.top, end_cell, visited,screen, isFirst) or \
           DFS(curr_cell.right, end_cell, visited,screen, isFirst) or \
           DFS(curr_cell.left, end_cell, visited, screen, isFirst) or \
           DFS(curr_cell.bottom, end_cell, visited, screen, isFirst)

def BFS(curr_cell, end_cell, visited, screen):
    q = deque()
    q.append(curr_cell)

    while q:
        curr_cell = q.popleft()
        # Base case
        if (curr_cell.row == end_cell.row and curr_cell.col == end_cell.col):
            return True
        visited.add((curr_cell.row, curr_cell.col))

        if curr_cell.top and (curr_cell.top.row, curr_cell.top.col) not in visited:
            q.append(curr_cell.top)
        if curr_cell.right and (curr_cell.right.row, curr_cell.right.col) not in visited:
            q.append(curr_cell.right)
        if curr_cell.bottom and (curr_cell.bottom.row, curr_cell.bottom.col) not in visited:
            q.append(curr_cell.bottom)
        if curr_cell.left and (curr_cell.left.row, curr_cell.left.col) not in visited:
            q.append(curr_cell.left)
        curr_cell.cell_surf.fill('Pink')
        screen.blit(curr_cell.cell_surf, curr_cell.cell_surf_rect)
        pygame.display.update()
        pygame.time.delay(1)
    return False

    # q = deque()
    # q.append((curr_cell.row, curr_cell.col))
    #
    # while q:
    #     curr_row, curr_col = q.popleft()
    #
    #     # Base case
    #     if curr_row == end_cell.row and curr_col == end_cell.col:
    #         return True
    #     visited.add((curr_row, curr_col))
    #
    #     for t in [(1,0),(-1,0),(0,1),(0,-1)]:
    #         if curr_row + t[0] < 0 or curr_row + t[0] >= len(cells) or curr_col + t[1] < 0 or curr_col + t[0] >= len(cells[0]) or \
    #             (curr_row + t[0], curr_col + t[1]) in visited:
    #             continue
    #         else:
    #             q.append((curr_row + t[0], curr_col + t[1]))
    #
    #     screen.blit(cells[curr_row][curr_col].cell_surf, cells[curr_row][curr_col].cell_surf_rect)
    #     pygame.display.update()
    #     pygame.time.delay(2)
    # return False


    # q = []
    # while q:
    #     q_len = len(q)
    #     for i in range(q_len):
    #         curr_cell = q[i]
    #         if (curr_cell.row == end_cell.row and curr_cell.col == end_cell.col):
    #             return True
    #         visited.add((curr_cell.row, curr_cell.col))
    #         if curr_cell.top and (curr_cell.top.row, curr_cell.top.col) not in visited:
    #             q.append(curr_cell.top)
    #         if curr_cell.right and (curr_cell.right.row, curr_cell.right.col) not in visited:
    #             q.append(curr_cell.right)
    #         if curr_cell.bottom and (curr_cell.bottom.row, curr_cell.bottom.col) not in visited:
    #             q.append(curr_cell.bottom)
    #         if curr_cell.left and (curr_cell.left.row, curr_cell.left.col) not in visited:
    #             q.append(curr_cell.left)



def main():

    # Initialize pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Menu screen
    dfs_button = pygame.image.load('Art/Buttons/DFS_button.png').convert_alpha()
    dfs_button_rect = dfs_button.get_rect(center = (650,100))

    bfs_button = pygame.image.load('Art/Buttons/BFS_button.png').convert_alpha()
    bfs_button_rect = bfs_button.get_rect(center = (650,200))

    # Chosen algorithm
    chosen_algorithm = None

    # Starting point surface
    starting_point_surf = None

    # End point surface
    end_point_surf = None

    # Obstacles
    obstacles = set()
    visited = set()


    # Visualizer status
    is_menu_screen = True
    is_placing_s_point, is_placing_e_point = False, False
    is_placing_obstacles, is_visualizing = False, False


    # Create cells
    cells = CreateCells(SCREEN_HEIGHT, SCREEN_WIDTH, CELL_HEIGHT, CELL_WIDTH, HEIGHT_PAD, SIDE_PAD)
    ROWS, COLS = len(cells), len(cells[0])

    while True:
        # Background
        screen.fill('White')


        if is_menu_screen:
            screen.blit(dfs_button,dfs_button_rect)
            screen.blit(bfs_button, bfs_button_rect)

        # Handle different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Place starting and end point
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_menu_screen:
                    if dfs_button_rect.collidepoint((event.pos[0], event.pos[1])):
                        chosen_algorithm = 'dfs'
                        is_menu_screen = False
                        is_placing_s_point = True
                    elif bfs_button_rect.collidepoint((event.pos[0], event.pos[1])):
                        chosen_algorithm = 'bfs'
                        is_menu_screen = False
                        is_placing_s_point = True

                elif isPosWithinCells(event.pos[0], event.pos[1], SCREEN_HEIGHT, SCREEN_WIDTH, SIDE_PAD, HEIGHT_PAD):
                    pos_x, pos_y = event.pos[0], event.pos[1]
                    r, c = getRowAndCol(pos_x, pos_y, SIDE_PAD, HEIGHT_PAD, CELL_WIDTH, CELL_HEIGHT)
                    # Get starting point
                    if is_placing_s_point:
                        # pos_x, pos_y = event.pos[0], event.pos[1]
                        # s_row, s_col = getRowAndCol(pos_x, pos_y, SIDE_PAD, HEIGHT_PAD, CELL_WIDTH, CELL_HEIGHT)
                        s_row, s_col = r, c
                        starting_point_surf = cells[s_row][s_col].cell_surf
                        starting_point_surf.fill('Red')

                    # Get end point
                    if is_placing_e_point and not (r == s_row and c == s_col):
                        # pos_x, pos_y = event.pos[0], event.pos[1]
                        # e_row, e_col = getRowAndCol(pos_x, pos_y, SIDE_PAD, HEIGHT_PAD, CELL_WIDTH, CELL_HEIGHT)
                        e_row, e_col = r, c
                        end_point_surf = cells[e_row][e_col].cell_surf
                        end_point_surf.fill('Blue')

                    # Get obstacles
                    if is_placing_obstacles and not (r == s_row and c == s_col) and not (r == e_row and c == e_col):
                        o_row, o_col = r, c
                        obs = cells[o_row][o_col]
                        if (obs.row, obs.col) not in visited:
                            obs.cell_surf.fill('Black')
                            obstacles.add(obs)
                            visited.add((obs.row, obs.col))


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_placing_s_point and starting_point_surf is not None:
                        is_placing_s_point = False
                        is_placing_e_point = True
                    elif is_placing_e_point and end_point_surf is not None:
                        is_placing_e_point = False
                        is_placing_obstacles = True
                    elif is_placing_obstacles:
                        is_placing_obstacles = False
                        is_visualizing = True


        # Drawing cells
        if not is_menu_screen:
            DrawCells(cells, screen, CELL_COLOR)

        # Draw the starting point
        if starting_point_surf is not None:
            screen.blit(starting_point_surf,(cells[s_row][s_col].pos_x, cells[s_row][s_col].pos_y))
        # Draw the messages when the user is choosing the starting point
        if is_placing_s_point:
            drawTextOnStartingPointScreen(screen)

        # Draw the end point
        if end_point_surf is not None:
            screen.blit(end_point_surf, (cells[e_row][e_col].pos_x, cells[e_row][e_col].pos_y))
        # Draw the message when the user is choosing the end point
        if is_placing_e_point:
            drawTextOnEndPointScreen(screen)

        # Draw the obstacles
        if len(obstacles) > 0:
            for obs in obstacles:
                screen.blit(obs.cell_surf, (cells[obs.row][obs.col].pos_x, cells[obs.row][obs.col].pos_y))
        # Draw the message when the user is placing obstacles
        if is_placing_obstacles:
            drawTextOnObstacleScreen(screen)

        # Visulize the algorithm
        if is_visualizing:
            # Visualize DFS
            if chosen_algorithm == 'dfs':
                isEndPointReached = DFS(cells[s_row][s_col], cells[e_row][e_col], visited, screen)
                # isEndPointReached = BFS(cells[s_row][s_col], cells[e_row][e_col], visited, screen)
                is_visualizing = False
            # Visualize BFD
            elif chosen_algorithm == 'bfs':
                isEndPointReached = BFS(cells[s_row][s_col], cells[e_row][e_col], visited, screen)


        if not is_visualizing and not is_placing_s_point and not is_placing_e_point and not is_placing_obstacles:
            for row, col in visited:
                cell = cells[row][col]
                screen.blit(cell.cell_surf,cell.cell_surf_rect)
















        clock.tick(60)
        pygame.display.update()



if __name__ == "__main__":
    main()

