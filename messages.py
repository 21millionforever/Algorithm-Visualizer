import pygame

# Text font
pygame.font.init()
text_font = pygame.font.SysFont('Normal text', 40)

# Messages when the user is placing the starting point
placing_s_message = text_font.render('Please choose a starting point by clicking on any of the cells', True, 'Red')
placeing_s_message_rect = placing_s_message.get_rect(center=(650, 50))

finish_s_message_1 = text_font.render('Once you have chosen a starting point, ', True, 'Red')
finish_s_message_rect_1 = finish_s_message_1.get_rect(center=(650, 640))

finish_s_message_2 = text_font.render('click Square to continue to the next step', True, 'Red')
finish_s_message_rect_2 = finish_s_message_2.get_rect(center=(650, 670))

# Messages when the user is placing the end point
placing_e_message = text_font.render('Please choose an end point by clicking on any of the cells', True, 'Blue')
placing_e_message_rect = placing_e_message.get_rect(center=(650, 50))

finish_e_message_1 = text_font.render('Once you have chosen an end point, ', True, 'Blue')
finish_e_message_rect_1 = finish_e_message_1.get_rect(center=(650, 640))

finish_e_message_2 = text_font.render('click Square to continue to the next step', True, 'Blue')
finish_e_message_rect_2 = finish_e_message_2.get_rect(center=(650, 670))


# Messages when the user is placing the obstacles
placing_o_messgae = text_font.render('Please place one or many obstacles', True, 'Black')
placing_o_messgae_rect = placing_o_messgae.get_rect(center=(650, 50))

finish_o_messgae_1 = text_font.render('Once you have placed all the obstacles, ', True, 'Black')
finish_o_messgae_rect_1 = finish_o_messgae_1.get_rect(center=(650, 640))

finish_o_messgae_2 = text_font.render('click Square to visualize the algorithm', True, 'Black')
finish_o_messgae_rect_2 = finish_o_messgae_2.get_rect(center=(650, 670))





def drawTextOnStartingPointScreen(screen):
    screen.blit(placing_s_message, placeing_s_message_rect)
    screen.blit(finish_s_message_1, finish_s_message_rect_1)
    screen.blit(finish_s_message_2, finish_s_message_rect_2)

def drawTextOnEndPointScreen(screen):
    screen.blit(placing_e_message, placing_e_message_rect)
    screen.blit(finish_e_message_1, finish_e_message_rect_1)
    screen.blit(finish_e_message_2, finish_e_message_rect_2)


def drawTextOnObstacleScreen(screen):
    screen.blit(placing_o_messgae, placing_o_messgae_rect)
    screen.blit(finish_o_messgae_1, finish_o_messgae_rect_1)
    screen.blit(finish_o_messgae_2, finish_o_messgae_rect_2)