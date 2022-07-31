import pygame

pygame.font.init()
text_font = pygame.font.SysFont('Normal text', 40)

# Messages needed when the user is choosing the starting point
choose_s_message = text_font.render('Please choose a starting point by clicking on any of the cells', True, 'Red')
choose_s_message_rect = choose_s_message.get_rect(center=(650, 50))

finish_s_message_1 = text_font.render('Once you have chosen a starting point, ', True, 'Red')
finish_s_message_rect_1 = finish_s_message_1.get_rect(center=(650, 640))

finish_s_message_2 = text_font.render('click Square to continue to the next step', True, 'Red')
finish_s_message_rect_2 = finish_s_message_2.get_rect(center=(650, 670))

# Messages needed when the user is choosing the end point
choose_e_message = text_font.render('Please choose an end point by clicking on any of the cells', True, 'Red')
choose_e_message_rect = choose_e_message.get_rect(center=(650, 50))

finish_e_message_1 = text_font.render('Once you have chosen an end point, ', True, 'Red')
finish_e_message_rect_1 = finish_e_message_1.get_rect(center=(650, 640))

finish_e_message_2 = text_font.render('click Square to continue to the next step', True, 'Red')
finish_e_message_rect_2 = finish_e_message_2.get_rect(center=(650, 670))


def drawTextOnStartingPointScreen(screen):
    screen.blit(choose_s_message, choose_s_message_rect)
    screen.blit(finish_s_message_1, finish_s_message_rect_1)
    screen.blit(finish_s_message_2, finish_s_message_rect_2)

def drawTextOnEndPointScreen(screen):
    screen.blit(choose_e_message, choose_e_message_rect)
    screen.blit(finish_e_message_1, finish_e_message_rect_1)
    screen.blit(finish_e_message_2, finish_e_message_rect_2)