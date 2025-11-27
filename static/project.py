import pygame
from sys import exit
import random
#--------------------
#these are the colors I want to use in my game:
gray_blue_dk = (30, 38, 28)
gray_blue_lgt = (45, 55, 70)
cyan_neon = (0, 255, 255)
cyan_soft = (100, 230, 255)
white = (255, 255, 255)
black = (0, 0, 0)
play_cyan = (0, 255, 220)
exit_red = (255, 50, 80)
#--------------------
pygame.init()
font = pygame.font.Font(None, 46)

#--------------------this is the "display surface":

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Codeborn: Meet OptiDawn")
clock = pygame.time.Clock()

#--------------------(I want to use this seperator like I did for my notes to keep it looking clean)
#I'm going to name and add my files here to make it easy for me to stay organized and keep it all together

start_screen = pygame.image.load("startscreen.png").convert_alpha()
start_screen = pygame.transform.smoothscale(start_screen, (1000,700))
#--------------------
bg_list = [pygame.image.load("Background.png").convert_alpha(), pygame.image.load("BG1.png").convert_alpha(),
           pygame.image.load("BG2.png").convert_alpha(), pygame.image.load("BG3.png").convert_alpha(),
           pygame.image.load("BG4.png").convert_alpha()]

for b in range(len(bg_list)):
    bg_list[b] = pygame.transform.smoothscale(bg_list[b], (1000, 700))
current_bg = 0
#--------------------
good_list = [pygame.image.load("CG1.png").convert_alpha(),pygame.image.load("CG2.png").convert_alpha(),
             pygame.image.load("CG3.png").convert_alpha(), pygame.image.load("CG4.png").convert_alpha(),
             pygame.image.load("CG5.png").convert_alpha(),pygame.image.load("OptiDawn.png").convert_alpha()]
#--------------------
bad_list = [pygame.image.load("RB1.png").convert_alpha(), pygame.image.load("RB2.png").convert_alpha(),
            pygame.image.load("RB3.png").convert_alpha(), pygame.image.load("RB4.png").convert_alpha(),
            pygame.image.load("RB5.png").convert_alpha(), pygame.image.load("OptiFail.png").convert_alpha()]
#--------------------
game_state = "startup"
username = ""
play_button = pygame.Rect(90, 380, 300, 70)
exit_button = pygame.Rect(170, 460, 140, 60)
running = True
#-------------------- add events area
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif game_state == "startup":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_state = "game"
                if exit_button.collidepoint(event.pos):
                    running = False

        elif game_state == "boot_sequence":
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "name_input"

        elif event.type == pygame.KEYDOWN:
            if game_state == "name_input":
                if event.key == pygame.K_RETURN:
                    if username != "":
                        game_state = "good_feedback"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if event.unicode.isalnum() and len(username) < 15:
                        username += event.unicode

        elif game_state == "good_feedback":
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_stage += 1
                game_state = "next_q"

        elif game_state == "bad_feedback":
            if event.type == pygame.MOUSEBUTTONDOWN:
                attempts_left -= 3
                if attempts_left <= 0:
                    game_state = "game_game"
                else:
                    game_state = "retry_q"

        elif game_state == "next_q":
            pass

        elif game_state == "retry_q":
            pass

        elif game_state == "g_game":
            pass



#-------------------- startup gs

    if game_state == "startup":
        screen.blit(start_screen, (0, 0))

    elif game_state == "game":
        screen.blit(bg_list[current_bg], (0, 0))

        if current_bg < 4:
            messages = [
                ["...(click anywhere)"],

                ["Helion Protocol: Finally..(click anywhere)"],

                ["Helion Protocol: I've been waiting for",
                 "someone like you. (click anywhere)"]
                ]
            lines = messages[current_bg]
            y = 560
            for line in lines:
                text = font.render(line, True, white)
                text_rect = text.get_rect(center=(500, y))
                screen.blit(text, text_rect)
                y += 50

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if current_bg < len(bg_list) - 1:
                    current_bg += 1
                    pygame.time.wait(300)
                else:
                    game_state = "boot_sequence"

#-------------------- boot sequence gs

    elif game_state == "boot_sequence":
        screen.fill(black)
        elogs = [
            "[ SYSTEM WAKE PROTOCOL... FAILED ]",
            "[ SIGNAL COHERENCE... 12% ]",
            "[ STARLINK PING... 34ms ]"
            ]
        y = 300
        for log in elogs:
            text = font.render(log, True, cyan_soft)
            rect = text.get_rect(center=(500, y))
            screen.blit(text, rect)
            y += 70

#-------------------- name input gs

    elif game_state == "name_input":
        screen.blit(bg_list[4],(0,0))

        etext = "[ IDENTIFYING OPERATOR... ]"
        ep_text = font.render(etext, True, cyan_soft)
        screen.blit(ep_text, ep_text.get_rect(center=(500,200)))

        prompt = ["Helion Protocol: Tell it your designation, engineer.",
                  "(type in your name and press enter)"]
        y = 300
        for line in prompt:
            text = font.render(line, True, white)
            text_rect = text.get_rect(center=(500, y))
            screen.blit(text, text_rect)
            y += 50

        input_area = pygame.Rect(300, 400, 400, 60)
        pygame.draw.rect(screen, gray_blue_lgt, input_area, border_radius=10)

        name_text = font.render(username.upper(), True, white)
        screen.blit(name_text, name_text.get_rect(center=(500,430)))
        game_state = "good_Feedback"


    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()