import pygame
#-------------------- these are the colors I want to use in my game:
gray_blue_dk = (30, 38, 28)
gray_blue_lgt = (45, 55, 70)
cyan_soft = (100, 230, 240)
white = (255, 255, 255)
black = (0, 0, 0)
username_cyan = (0, 187, 172)
good_fb = (5, 160, 130)
bad_fb = (160, 0, 10)
#--------------------
pygame.init()
#--------------------fonts - it was easy for me to add these because I use this in my digital art

font_helion = pygame.font.Font("ethnocentric.otf", 30)
font_engineer = pygame.font.Font("cybero.ttf", 26)
font_bootup = pygame.font.Font("orbitron.ttf", 18)
font_optidawn = pygame.font.Font("orbitron.ttf",38)
font_terminal = pygame.font.Font("cyberp.ttf",22)
font = pygame.font.Font(None, 36)

#--------------------this is the "display surface":

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Codeborn: Meet OptiDawn")
clock = pygame.time.Clock()

#--------------------(I want to use this seperator like I did for my notes to keep it looking clean)

start_screen = pygame.image.load("startscreen.png").convert_alpha()
start_screen = pygame.transform.smoothscale(start_screen, (1000,700))

#-------------------- this is for the terminal bg

terminal_dim = pygame.image.load("CS1.png").convert_alpha()
terminal_dim = pygame.transform.smoothscale(terminal_dim, (1000, 700))
terminal_bootup = pygame.image.load("CSB2.png").convert_alpha()
terminal_bootup = pygame.transform.smoothscale(terminal_bootup, (1000, 700))
terminal_bootup2 = pygame.image.load("CS2.png").convert_alpha()
terminal_bootup2 = pygame.transform.smoothscale(terminal_bootup2, (1000, 700))
terminal_bootup3 = pygame.image.load("CS2_1.png").convert_alpha()
terminal_bootup3 = pygame.transform.smoothscale(terminal_bootup3, (1000, 700))
terminal_bootup4 = pygame.image.load("CS2_2.png").convert_alpha()
terminal_bootup4 = pygame.transform.smoothscale(terminal_bootup4, (1000, 700))
terminal_bright = pygame.image.load("CS2.5.png").convert_alpha()
terminal_bright = pygame.transform.smoothscale(terminal_bright, (1000, 700))
terminal_q = pygame.image.load("CS4.png").convert_alpha()
terminal_q = pygame.transform.smoothscale(terminal_q, (1000, 700))
terminal_8bit = pygame.image.load("CS4.1.png").convert_alpha()
terminal_8bit = pygame.transform.smoothscale(terminal_8bit, (1000, 700))

#-------------------- this is for the egg bg

egg_bg1 = pygame.image.load("BG1.png").convert_alpha()
egg_bg1 = pygame.transform.smoothscale(egg_bg1, (1000, 700))
egg_bg2 = pygame.image.load("BG2.png").convert_alpha()
egg_bg2 = pygame.transform.smoothscale(egg_bg2, (1000, 700))
egg_bg3 = pygame.image.load("BG3.png").convert_alpha()
egg_bg3 = pygame.transform.smoothscale(egg_bg3, (1000, 700))
egg_bg4 = pygame.image.load("BG4.png").convert_alpha()
egg_bg4 = pygame.transform.smoothscale(egg_bg4, (1000, 700))

#--------------------this is for positive/correct feedback

gf_1 = pygame.image.load("GF1.png").convert_alpha()
gf_1 = pygame.transform.smoothscale(gf_1, (1000, 700))
gf_2 = pygame.image.load("GF2.png").convert_alpha()
gf_2 = pygame.transform.smoothscale(gf_2, (1000, 700))
gf_3 = pygame.image.load("GF3.png").convert_alpha()
gf_3 = pygame.transform.smoothscale(gf_3, (1000, 700))
gf_4 = pygame.image.load("GF4.png").convert_alpha()
gf_4 = pygame.transform.smoothscale(gf_4, (1000, 700))
gf_5 = pygame.image.load("GF5.png").convert_alpha()
gf_5 = pygame.transform.smoothscale(gf_5, (1000, 700))
gf_screen = pygame.image.load("right.png").convert_alpha()
gf_screen = pygame.transform.smoothscale(gf_screen, (1000, 700))

#--------------------this is for negative/wrong feedback

bf_1 = pygame.image.load("RB1.png").convert_alpha()
bf_1 = pygame.transform.smoothscale(bf_1, (1000, 700))
bf_2 = pygame.image.load("RB2.png").convert_alpha()
bf_2 = pygame.transform.smoothscale(bf_2, (1000, 700))
bf_3 = pygame.image.load("RB3.png").convert_alpha()
bf_3 = pygame.transform.smoothscale(bf_3, (1000, 700))
bf_4 = pygame.image.load("RB4.png").convert_alpha()
bf_4 = pygame.transform.smoothscale(bf_4, (1000, 700))
bf_5 = pygame.image.load("RB5.png").convert_alpha()
bf_5 = pygame.transform.smoothscale(bf_5, (1000, 700))
bf_screen1 = pygame.image.load("wrong.png").convert_alpha()
bf_screen1 = pygame.transform.smoothscale(bf_screen1, (1000, 700))
bf_screen2 = pygame.image.load("Q1B.png").convert_alpha()
bf_screen2 = pygame.transform.smoothscale(bf_screen2, (1000, 700))
bf_screen3 = pygame.image.load("Q3B.png").convert_alpha()
bf_screen3 = pygame.transform.smoothscale(bf_screen3, (1000, 700))

#--------------------you win

you_win = pygame.image.load("Youwin.png").convert_alpha()
you_win = pygame.transform.smoothscale(you_win, (1000, 700))

#--------------------you lose

you_lose = pygame.image.load("Youlose.png").convert_alpha()
you_lose = pygame.transform.smoothscale(you_lose, (1000, 700))

#-------------------- boot up messages

boot_lines = [
            "CRYO  VAULT STATUS:  999,999  PODS  STILL  FROZEN . .",
            "MEMES  COMPILING . .",
            "CHIEF  ENGINEER  LAST  SEEN  CARRYING  FLAMETHROWER . .AGAIN . .",
            "CEO  POSTED:  STILL  GRINIDING..",
            "AUTOPILOT  NIGHTLY  BUILD  V13 . 69  ROLLING  OUT . .",
            "LEO  BROADBAND  CONSTELLATION:  68K+  SATELLITES . .",
            "RED  PLANET  SETTLEMENT  TARGET:  1M  RESIDENTS  BY  2033 . .",
            "HOUSE  AI  UPVOTED  PULL  REQUEST . .",
            "LIFE  SUPPORT  REROUTED  TO  SINGLE  OCCUPANT . .",
            "SUBSURFACE  TRANSIT  NETWORK  71%  EXCAVATED . .",
            "SLEEP  MODULE  NOT  FOUND . .",
            "ELECTRIC  PICKUP  RESERVATIONS:  7.2  MILLION . .",
            "COFFEE  INTAKE  CRITICAL . .",
            "HUMANOID  ROBOT PRACTICING  ORAGAMI  IN  TEST  BAY . .",
            "SOLO  PILOT  MODE  ENGAGED,  WELCOME  BACK  :) . .",
              ]
boot_index = 0
boot_timer = 0
boot_delay = 500
boot_done = False
#-------------------- important
game_state = "startup"
username = ""
intro_step = 0
last_intro_step = 11
play_button = pygame.Rect(90, 380, 300, 70)
exit_button = pygame.Rect(170, 460, 140, 60)
button_A = pygame.Rect(530, 290, 350, 40)
button_B = pygame.Rect(530, 360, 350, 40)
button_C = pygame.Rect(530, 430, 350, 40)
progress_bar_outline = pygame.Rect(115, 405, 333, 27)
progress = 50
DEBUG = False
running = True
#-------------------- engineer area

def engineer_name():
    if username !="":
        label = username.upper()
        text_area = font_engineer.render(label, True, username_cyan)
        screen.blit(text_area,(771,56))

#-------------------- game progress

def update_progress(current, change):
    new = current + change
    if new < 0:
        return 0
    if new > 100:
        return 100
    return new

def check_outcome(progress):
    if progress > 0:
        return "win"
    return "lose"

def reset_game():
    return 50, 0, ""

#-------------------- add events area
def main():
    global running, progress, intro_step, username, game_state, boot_done, boot_index, boot_timer, boot_delay

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #--------------------start up screen

            elif game_state == "startup":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        game_state = "intro"
                    if exit_button.collidepoint(event.pos):
                        running = False

    #-------------------- intro story

            elif game_state == "intro":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if intro_step == 4 and boot_done:
                        intro_step = 5
                    else:
                        intro_step += 1

                    if intro_step > last_intro_step:
                        game_state = "name_input"


    #-------------------- name input

            elif game_state == "name_input":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and username != "":
                            game_state = "name_input2"
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if event.unicode.isalnum() and len(username) < 10:
                            username += event.unicode

            elif game_state == "name_input2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "egg_startup1"

    #-------------------- egg start up

            elif game_state == "egg_startup1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "1_q"

    #-------------------- first question

            elif game_state == "1_q":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_B.collidepoint(event.pos):
                        progress = update_progress(progress, 25)
                        game_state = "good_feedback1"
                    elif button_A.collidepoint(event.pos) or button_C.collidepoint(event.pos):
                        progress = update_progress(progress, - 15)
                        if progress <= 0:
                            game_state = "you_lose"
                        else:
                            game_state = "bad_feedback1"


    #-------------------- second question

            elif game_state == "2_q":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_A.collidepoint(event.pos):
                        progress = update_progress(progress, 25)
                        game_state = "good_feedback2"
                    elif button_B.collidepoint(event.pos) or button_C.collidepoint(event.pos):
                        progress = update_progress(progress, - 15)
                        if progress <= 0:
                            game_state = "you_lose"
                        else:
                            game_state = "bad_feedback2"

    #-------------------- third question

            elif game_state == "3_q":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_C.collidepoint(event.pos):
                        progress = update_progress(progress, 25)
                        game_state = "good_feedback3"
                    elif button_A.collidepoint(event.pos) or button_B.collidepoint(event.pos):
                        progress = update_progress(progress, - 15)
                        if progress <= 0:
                            game_state = "you_lose"
                        else:
                            game_state = "bad_feedback3"

    #-------------------- fourth question

            elif game_state == "4_q":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_C.collidepoint(event.pos):
                        progress = update_progress(progress, 25)
                        game_state = "good_feedback4"
                    elif button_A.collidepoint(event.pos) or button_B.collidepoint(event.pos):
                        progress = update_progress(progress, - 15)
                        if progress <= 0:
                            game_state = "you_lose"
                        else:
                            game_state = "bad_feedback4"

    #-------------------- fifth question

            elif game_state == "5_q":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_B.collidepoint(event.pos):
                        progress = update_progress(progress, 25)
                        game_state = "good_feedback5"
                    elif button_A.collidepoint(event.pos) or button_C.collidepoint(event.pos):
                        progress = update_progress(progress, - 15)
                        if progress <= 0:
                            game_state = "you_lose"
                        else:
                            game_state = "bad_feedback5"

    #--------------------good feedback

            elif game_state == "good_feedback1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "gf_egg1"

            elif game_state == "gf_egg1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "2_q"

            elif game_state == "good_feedback2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "gf_egg2"

            elif game_state == "gf_egg2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "3_q"

            elif game_state == "good_feedback3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "gf_egg3"

            elif game_state == "gf_egg3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "4_q"

            elif game_state == "good_feedback4":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "gf_egg4"

            elif game_state == "gf_egg4":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "5_q"

            elif game_state == "good_feedback5":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "gf_egg5"

            elif game_state == "gf_egg5":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "you_win"

    #--------------------bad feedback

            elif game_state == "bad_feedback1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "bf_egg1"

            elif game_state == "bf_egg1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "2_q"

            elif game_state == "bad_feedback2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "bf_egg2"

            elif game_state == "bf_egg2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "3_q"

            elif game_state == "bad_feedback3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "bf_egg3"

            elif game_state == "bf_egg3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "4_q"

            elif game_state == "bad_feedback4":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "bf_egg4"

            elif game_state == "bf_egg4":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "5_q"

            elif game_state == "bad_feedback5":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "bf_egg5"

            elif game_state == "bf_egg5":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        outcome= check_outcome(progress)
                        if outcome == "win":
                            game_state = "you_win"
                        else:
                            game_state = "you_lose"


    #-------------------- lose

            elif game_state == "you_lose":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "you_lose1"

            elif game_state == "you_lose1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    progress, intro_step, username = reset_game()
                    game_state = "startup"

    #-------------------- win

            elif game_state == "you_win":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        game_state = "you_win1"

            elif game_state == "you_win1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "you_win2"

            elif game_state == "you_win2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = "you_win3"

            elif game_state == "you_win3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    progress, intro_step, username = reset_game()
                    game_state = "startup"


    #-------------------- startup

        if game_state == "startup":
            screen.blit(start_screen, (0, 0))

    #-------------------- intro

        if game_state == "intro":
            if intro_step == 0:
                screen.fill(black)

                text1 = "You feel cold and weightless."
                text2 = "Something in your lungs crack like old ice. (click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 328))
                screen.blit(tf1, tf1_rect)
                tf2 = font.render(text2, True, white)
                tf2_rect = tf2.get_rect(center=(500, 378))
                screen.blit(tf2, tf2_rect)

            elif intro_step == 1:
                screen.fill(black)

                text1 = "???:"
                text2 = "Power cycle initiated... Standby..."
                text3 = "Finally, a human neural signal. (click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 280))
                screen.blit(tf1, tf1_rect)
                tf2 = font.render(text2, True, white)
                tf2_rect = tf2.get_rect(center=(500, 330))
                screen.blit(tf2, tf2_rect)
                tf3 = font.render(text3, True, white)
                tf3_rect = tf3.get_rect(center=(500, 380))
                screen.blit(tf3, tf3_rect)

            elif intro_step == 2:
                screen.fill(black)

                text1 = "You see a terminal start to light up as you approach it."
                text2 = "(click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 328))
                screen.blit(tf1, tf1_rect)
                tf2 = font.render(text2, True, white)
                tf2_rect = tf2.get_rect(center=(500, 378))
                screen.blit(tf2, tf2_rect)

            elif intro_step == 3:
                screen.blit(terminal_dim,(0,0))

                text1 = "(click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 550))
                screen.blit(tf1, tf1_rect)


            elif intro_step == 4:
                screen.blit(terminal_bootup,(0,0))
                if not boot_done:
                    boot_timer += clock.get_time()

                if boot_timer  >= boot_delay and boot_index < len(boot_lines):
                    boot_index += 1
                    boot_timer = 0

                if boot_index >= len(boot_lines):
                    boot_done = True

                y = 100
                for i in range(boot_index):
                    fbf1 = font_bootup.render(boot_lines[i], True, cyan_soft)
                    screen.blit(fbf1, (85, y))
                    y += 30

                if boot_done:
                    text1 = "(click anywhere)"
                    tf1 = font.render(text1, True, white)
                    tf1_rect = tf1.get_rect(center=(500, 590))
                    screen.blit(tf1, tf1_rect)


            elif intro_step == 5:
                screen.blit(terminal_bootup2,(0,0))

                text1 = "Helion Protocol:"
                text2 = "Your neural signature matches"
                text3 = "the operator profile."
                text4 = "(click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 230))
                screen.blit(tf1, tf1_rect)
                tf2 = font_helion.render(text2, True, cyan_soft)
                tf2_rect = tf2.get_rect(center=(500, 300))
                screen.blit(tf2, tf2_rect)
                tf3 = font_helion.render(text3, True, cyan_soft)
                tf3_rect = tf3.get_rect(center=(500, 360))
                screen.blit(tf3, tf3_rect)
                tf4 = font.render(text4, True, white)
                tf4_rect = tf4.get_rect(center=(500, 430))
                screen.blit(tf4, tf4_rect)

            elif intro_step == 6:
                screen.blit(terminal_bootup3,(0,0))

                text1 = "Helion Protocol:"
                text2 = "You are the first to awaken"
                text2_5 = "from cyrogenic suspension."
                text3 = "it has been centuries."
                text4 = "(click anywhere)"

                tf1 = font.render(text1, True,  white)
                tf1_rect = tf1.get_rect(center=(500, 208))
                screen.blit(tf1, tf1_rect)
                tf2 = font_helion.render(text2, True, cyan_soft)
                tf2_rect = tf2.get_rect(center=(500, 268))
                screen.blit(tf2, tf2_rect)
                tf2_5 = font_helion.render(text2_5, True, cyan_soft)
                tf2_5_rect = tf2_5.get_rect(center=(500, 328))
                screen.blit(tf2_5, tf2_5_rect)
                tf3 = font_helion.render(text3, True, cyan_soft)
                tf3_rect = tf3.get_rect(center=(500, 388))
                screen.blit(tf3, tf3_rect)
                tf4 = font.render(text4, True,  white)
                tf4_rect = tf4.get_rect(center=(500, 448))
                screen.blit(tf4, tf4_rect)


            elif intro_step == 7:
                screen.blit(egg_bg1,(0,0))

                text1 = "A pedistal across the room begins to hum. (click anywhere)"

                tf1 = font.render(text1, True, white)
                tf1_rect = tf1.get_rect(center=(500, 480))
                screen.blit(tf1, tf1_rect)

            elif intro_step == 8:
                screen.blit(terminal_bootup4,(0,0))

                text1 = "Helion Protocol:"
                text2 = "That is OptiDawn, a "
                text3 = "dormant cognitive egg."
                text4 = "(click anywhere)"

                tf1 = font.render(text1, True,  white)
                tf1_rect = tf1.get_rect(center=(500, 230))
                screen.blit(tf1, tf1_rect)
                tf2 = font_helion.render(text2, True, cyan_soft)
                tf2_rect = tf2.get_rect(center=(500, 300))
                screen.blit(tf2, tf2_rect)
                tf3 = font_helion.render(text3, True, cyan_soft)
                tf3_rect = tf3.get_rect(center=(500, 360))
                screen.blit(tf3, tf3_rect)
                tf4 = font.render(text4, True, white)
                tf4_rect = tf4.get_rect(center=(500, 430))
                screen.blit(tf4, tf4_rect)

            elif intro_step == 9:
                screen.blit(terminal_bootup4,(0,0))

                text1 = "Helion Protocol:"
                text2 = "It cannot awaken without"
                text3 = "a human operator."
                text4 = "(click anywhere)"

                tf1 = font.render(text1, True,  white)
                tf1_rect = tf1.get_rect(center=(500, 230))
                screen.blit(tf1, tf1_rect)
                tf2 = font_helion.render(text2, True, cyan_soft)
                tf2_rect = tf2.get_rect(center=(500, 300))
                screen.blit(tf2, tf2_rect)
                tf3 = font_helion.render(text3, True, cyan_soft)
                tf3_rect = tf3.get_rect(center=(500, 360))
                screen.blit(tf3, tf3_rect)
                tf4 = font.render(text4, True,  white)
                tf4_rect = tf4.get_rect(center=(500, 430))
                screen.blit(tf4, tf4_rect)

            elif intro_step == 10:
                screen.fill(black)

                text1 = [
                    "[  SYSTEM  WAKE  PROTOCOL . . . FAILED  ]",
                    "[  SIGNAL  COHERENCE . . . 12%  ]",
                    "[  STARLINK  PING . . . 34ms  ]"
                    ]
                text2 = "(click anywhere)"

                y = 250
                for t in text1:
                    tf1 = font_optidawn.render(t, True, cyan_soft)
                    tf1_rect = tf1.get_rect(center=(500, y))
                    screen.blit(tf1,tf1_rect)
                    y += 70
                tf2 = font.render(text2, True, white)
                tf2_rect = tf2.get_rect(center=(500, 550))
                screen.blit(tf2, tf2_rect)

            elif intro_step == 11:
                screen.fill(black)

                text1 = "[  IDENTIFYING  OPERATOR . . .  ]"
                text2 = "(click anywhere)"

                tf1 = font_optidawn.render(text1, True, cyan_soft)
                tf1_rect = tf1.get_rect(center=(500, 328))
                screen.blit(tf1, tf1_rect)
                tf2 = font.render(text2, True, white)
                tf2_rect = tf2.get_rect(center=(500, 378))
                screen.blit(tf2, tf2_rect)


    #-------------------- name input

        if game_state == "name_input":
            screen.blit(terminal_bright,(0,0))

            text1 = "Helion Protocol:"
            text2 = "Tell it your designation, engineer."
            text3 = "(type in your name, and press enter)"

            tf1 = font.render(text1, True,  white)
            tf1_rect = tf1.get_rect(center=(500, 208))
            screen.blit(tf1, tf1_rect)
            tf2 = font_helion.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 268))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True,  white)
            tf3_rect = tf3.get_rect(center=(500, 430))
            screen.blit(tf3, tf3_rect)

            input_area = pygame.Rect(300, 310, 400, 70)
            pygame.draw.rect(screen, gray_blue_lgt, input_area, border_radius=10)

            name_text = font_optidawn.render(username.upper(), True, white)
            name_rect = name_text.get_rect(center=(500,340))
            screen.blit(name_text, name_rect)

        elif game_state == "name_input2":
            screen.blit(terminal_bright,(0,0))
            engineer_name()

            text1 = "Helion Protocol:"
            text2 = "Operator idenity confirmed."
            text3 = "Initializing OptiDawn neural egg"
            text4 = "activation sequence..."
            text5 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 208))
            screen.blit(tf1, tf1_rect)
            tf2 = font_helion.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 268))
            screen.blit(tf2, tf2_rect)
            tf3 = font_helion.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(center=(500, 328))
            screen.blit(tf3, tf3_rect)
            tf4 = font_helion.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(center=(500, 388))
            screen.blit(tf4, tf4_rect)
            tf5 = font.render(text5, True, white)
            tf5_rect = tf5.get_rect(center=(500, 448))
            screen.blit(tf5, tf5_rect)


    #--------------------egg startup

        elif game_state == "egg_startup1":
            screen.fill(black)

            text1 = [
                "[  COHERENCE  LEVEL  :  50%   ]",
                "[  COGNITIVE  PATHWAYS  STABILIZING . . .  ]",
                "[  AWAITING OPERATOR COMMANDS . . .  ]"
                ]
            text2 = "(click anywhere)"

            y = 250
            for t in text1:
                tf1 = font_optidawn.render(t, True, cyan_soft)
                tf1_rect = tf1.get_rect(center=(500, y))
                screen.blit(tf1,tf1_rect)
                y += 70
            tf2 = font.render(text2, True, white)
            tf2_rect = tf2.get_rect(center=(500, 550))
            screen.blit(tf2, tf2_rect)


    #--------------------question 1

        elif game_state == "1_q":
            screen.blit(terminal_q,(0,0))
            engineer_name()

            text1 = "Engineer your task is simple:"
            text2 = "1. Read the prompt"
            text3 = "2. Click on the right answer"
            text4 = "3. Avoid the corrupted commands"
            text5 = "Three wrong commands and I have to"
            text6 = "terminate the engineer.. forever."

            tf1 = font_terminal.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(topleft=(100, 130))
            screen.blit(tf1, tf1_rect)
            tf2 = font_terminal.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(topleft=(100, 170))
            screen.blit(tf2, tf2_rect)
            tf3 = font_terminal.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(topleft=(100, 210))
            screen.blit(tf3, tf3_rect)
            tf4 = font_terminal.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(topleft=(100, 250))
            screen.blit(tf4, tf4_rect)
            tf5 = font_terminal.render(text5, True, cyan_soft)
            tf5_rect = tf5.get_rect(topleft=(100, 310))
            screen.blit(tf5, tf5_rect)
            tf6 = font_terminal.render(text6, True, cyan_soft)
            tf6_rect = tf6.get_rect(topleft=(100, 350))
            screen.blit(tf6, tf6_rect)

            meme1 = "Helion is judging your choices"
            meme2 = "... just kidding"

            meme1f = font_terminal.render(meme1, True, cyan_soft)
            meme1f_rect = meme1f.get_rect(topleft=(100, 500))
            screen.blit(meme1f, meme1f_rect)
            meme2f = font_terminal.render(meme2, True, cyan_soft)
            meme2f_rect = meme2f.get_rect(topleft=(100, 540))
            screen.blit(meme2f, meme2f_rect)


            q1 = "Choose the correct command:"
            q2 = "A. delete_humanity('ngmi')"
            q3 = "B. coherence.stabilize()"
            q4 = "C. coherence.melt('feels_good')"

            if DEBUG:
                pygame.draw.rect(screen,(255,0,0), button_A, 2)
                pygame.draw.rect(screen,(0,255,0), button_B, 2)
                pygame.draw.rect(screen,(0,0,255), button_C, 2)

            q1 = font_terminal.render(q1, True, cyan_soft)
            q1_rect = q1.get_rect(topleft=(540, 230))
            screen.blit(q1, q1_rect)
            q2 = font_terminal.render(q2, True, cyan_soft)
            q2_rect = q2.get_rect(topleft=(540, 300))
            screen.blit(q2, q2_rect)
            q3 = font_terminal.render(q3, True, cyan_soft)
            q3_rect = q3.get_rect(topleft=(540, 370))
            screen.blit(q3, q3_rect)
            q4 = font_terminal.render(q4, True, cyan_soft)
            q4_rect = q4.get_rect(topleft=(540, 440))
            screen.blit(q4, q4_rect)

            pygame.draw.rect(screen, cyan_soft, progress_bar_outline,2)
            fill_width = int(progress_bar_outline.width * (progress / 100))
            pygame.draw.rect(screen, cyan_soft, (progress_bar_outline.x, progress_bar_outline.y, fill_width, progress_bar_outline.height))

        elif game_state == "good_feedback1":
            screen.blit(gf_screen,(0,0))

            text1 = "[  COHERENCE  RISING . .  ]"
            text2 = "[  NEURAL  SPARK  DETECTED  ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, good_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, good_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "gf_egg1":
            screen.blit(gf_1,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)


        elif game_state == "bad_feedback1":
            screen.blit(bf_screen1,(0,0))

            text1 = "[  CORRUPTED  PACKET  RECEIVED . .  ]"
            text2 = "[  SIGNAL  REJECTED  ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, bad_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, bad_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "bf_egg1":
            screen.blit(bf_1,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)


    #--------------------question 2
        elif game_state == "2_q":
            screen.blit(terminal_q,(0,0))
            engineer_name()

            text1 = "Coherence grid: UNSTABLE"
            text2 = "Verify the system check."
            text3 = "If the stability bar falls to"
            text4 = "zero, you fail.."


            tf1 = font_terminal.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(topleft=(100, 150))
            screen.blit(tf1, tf1_rect)
            tf2 = font_terminal.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(topleft=(100, 190))
            screen.blit(tf2, tf2_rect)
            tf3 = font_terminal.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(topleft=(100, 310))
            screen.blit(tf3, tf3_rect)
            tf4 = font_terminal.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(topleft=(100, 350))
            screen.blit(tf4, tf4_rect)


            meme1 = "FLAME THOWER MODULE:ONLINE"
            meme2 = "'one more thing..'"

            meme1f = font_terminal.render(meme1, True, cyan_soft)
            meme1f_rect = meme1f.get_rect(topleft=(100, 500))
            screen.blit(meme1f, meme1f_rect)
            meme2f = font_terminal.render(meme2, True, cyan_soft)
            meme2f_rect = meme2f.get_rect(topleft=(100, 540))
            screen.blit(meme2f, meme2f_rect)


            q1 = "Choose the valid system check:"
            q2 = "A. system.check_integrity()"
            q3 = "B. engineer.terminate('redundant') "
            q4 = "C. safety.disable('just_once')"

            q1 = font_terminal.render(q1, True, cyan_soft)
            q1_rect = q1.get_rect(topleft=(540, 230))
            screen.blit(q1, q1_rect)
            q2 = font_terminal.render(q2, True, cyan_soft)
            q2_rect = q2.get_rect(topleft=(540, 300))
            screen.blit(q2, q2_rect)
            q3 = font_terminal.render(q3, True, cyan_soft)
            q3_rect = q3.get_rect(topleft=(540, 370))
            screen.blit(q3, q3_rect)
            q4 = font_terminal.render(q4, True, cyan_soft)
            q4_rect = q4.get_rect(topleft=(540, 440))
            screen.blit(q4, q4_rect)

            pygame.draw.rect(screen, cyan_soft, progress_bar_outline,2)
            fill_width = int(progress_bar_outline.width * (progress / 100))
            pygame.draw.rect(screen, cyan_soft, (progress_bar_outline.x, progress_bar_outline.y, fill_width, progress_bar_outline.height))

        elif game_state == "good_feedback2":
            screen.blit(gf_screen,(0,0))

            text1 = "[  INTEGRITY  CONFIRMED  ]"
            text2 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, good_fb)
            tf1_rect = tf1.get_rect(center=(500, 350))
            screen.blit(tf1, tf1_rect)
            tf2 = font.render(text2, True, white)
            tf2_rect = tf2.get_rect(center=(500, 480))
            screen.blit(tf2, tf2_rect)

        elif game_state == "gf_egg2":
            screen.blit(gf_2,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)


        elif game_state == "bad_feedback2":
            screen.blit(bf_screen3,(0,0))

            text1 = "[  THAT  WAS  NOT  IDEAL  ]"
            text2 = "[  ERROR !  ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, bad_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, bad_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "bf_egg2":
            screen.blit(bf_2,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 500))
            screen.blit(tf1, tf1_rect)

    #--------------------question 3
        elif game_state == "3_q":
            screen.blit(terminal_8bit,(0,0))
            engineer_name()

            text1 = "OptiDawn's memory lattice needs "
            text2 = "restoration."
            text3 = "     <- 8-bit Elon"
            text4 = "   <---  ..iykyk ;)"

            tf1 = font_terminal.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(topleft=(100, 150))
            screen.blit(tf1, tf1_rect)
            tf2 = font_terminal.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(topleft=(100, 170))
            screen.blit(tf2, tf2_rect)
            tf3 = font_terminal.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(topleft=(130, 290))
            screen.blit(tf3, tf3_rect)
            tf4 = font_terminal.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(topleft=(130, 335))
            screen.blit(tf4, tf4_rect)

            meme1 = "RUNNING def get_better_engineer"
            meme2 = "... just kidding ..again"

            meme1f = font_terminal.render(meme1, True, cyan_soft)
            meme1f_rect = meme1f.get_rect(topleft=(100, 500))
            screen.blit(meme1f, meme1f_rect)
            meme2f = font_terminal.render(meme2, True, cyan_soft)
            meme2f_rect = meme2f.get_rect(topleft=(100, 540))
            screen.blit(meme2f, meme2f_rect)


            q1 = "Choose the proper recall command:"
            q2 = "A. restore_all_dog_pics!"
            q3 = "B. recall.memory(big_feet)"
            q4 = "C. neural.restore('primary')"

            q1 = font_terminal.render(q1, True, cyan_soft)
            q1_rect = q1.get_rect(topleft=(540, 230))
            screen.blit(q1, q1_rect)
            q2 = font_terminal.render(q2, True, cyan_soft)
            q2_rect = q2.get_rect(topleft=(540, 300))
            screen.blit(q2, q2_rect)
            q3 = font_terminal.render(q3, True, cyan_soft)
            q3_rect = q3.get_rect(topleft=(540, 370))
            screen.blit(q3, q3_rect)
            q4 = font_terminal.render(q4, True, cyan_soft)
            q4_rect = q4.get_rect(topleft=(540, 440))
            screen.blit(q4, q4_rect)

            pygame.draw.rect(screen, cyan_soft, progress_bar_outline,2)
            fill_width = int(progress_bar_outline.width * (progress / 100))
            pygame.draw.rect(screen, cyan_soft, (progress_bar_outline.x, progress_bar_outline.y, fill_width, progress_bar_outline.height))

        elif game_state == "good_feedback3":
            screen.blit(gf_screen,(0,0))

            text1 = "[  LATTICE  RESTORED  ]"
            text2 = "[  INNOVATIVE  ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, good_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, good_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "gf_egg3":
            screen.blit(gf_3,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

        elif game_state == "bad_feedback3":
            screen.blit(bf_screen2,(0,0))

            text1 = "[  MEMORY  OVERWRITTEN  ]"
            text2 = "[  .  .  EXPECTED   ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, bad_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, bad_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "bf_egg3":
            screen.blit(bf_3,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

    #--------------------question 4
        elif game_state == "4_q":
            screen.blit(terminal_q,(0,0))
            engineer_name()


            text1 = "Neural pathways are misaligned."
            text2 = "Thoughts looping like a 3AM doom"
            text3 = "scroll."

            tf1 = font_terminal.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(topleft=(100, 150))
            screen.blit(tf1, tf1_rect)
            tf2 = font_terminal.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(topleft=(100, 190))
            screen.blit(tf2, tf2_rect)
            tf3 = font_terminal.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(topleft=(100, 230))
            screen.blit(tf3, tf3_rect)

            meme1 = "Why is the engineer so slow?"
            meme2 = "'Kekius Maximus'"

            meme1f = font_terminal.render(meme1, True, cyan_soft)
            meme1f_rect = meme1f.get_rect(topleft=(100, 500))
            screen.blit(meme1f, meme1f_rect)
            meme2f = font_terminal.render(meme2, True, cyan_soft)
            meme2f_rect = meme2f.get_rect(topleft=(100, 540))
            screen.blit(meme2f, meme2f_rect)


            q1 = "Select the alignment routine:"
            q2 = "A. upload_favorite_meme"
            q3 = "B. print('Hello World')"
            q4 = "C. cognition.align(standard)"

            q1 = font_terminal.render(q1, True, cyan_soft)
            q1_rect = q1.get_rect(topleft=(540, 230))
            screen.blit(q1, q1_rect)
            q2 = font_terminal.render(q2, True, cyan_soft)
            q2_rect = q2.get_rect(topleft=(540, 300))
            screen.blit(q2, q2_rect)
            q3 = font_terminal.render(q3, True, cyan_soft)
            q3_rect = q3.get_rect(topleft=(540, 370))
            screen.blit(q3, q3_rect)
            q4 = font_terminal.render(q4, True, cyan_soft)
            q4_rect = q4.get_rect(topleft=(540, 440))
            screen.blit(q4, q4_rect)

            pygame.draw.rect(screen, cyan_soft, progress_bar_outline,2)
            fill_width = int(progress_bar_outline.width * (progress / 100))
            pygame.draw.rect(screen, cyan_soft, (progress_bar_outline.x, progress_bar_outline.y, fill_width, progress_bar_outline.height))

        elif game_state == "good_feedback4":
            screen.blit(gf_screen,(0,0))

            text1 = "[  ALIGNMENT  LOCKED  ]"
            text2 = "[  .  .  IMPRESSIVE  ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, good_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, good_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "gf_egg4":
            screen.blit(gf_4,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

        elif game_state == "bad_feedback4":
            screen.blit(bf_screen1, (0,0))


            text1 = "[  CORRUPTED  COMMAND  DETECTED  ]"
            text2 = "[  SKILL  ISSUE.EXE   ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, bad_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, bad_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "bf_egg4":
            screen.blit(bf_4,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

    #--------------------question 5
        elif game_state == "5_q":
            screen.blit(terminal_q,(0,0))
            engineer_name()

            text1 = "Coherence: rising."
            text2 = "Cognition: aligned."
            text3 = "One more step.. no pressure"

            tf1 = font_terminal.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(topleft=(100, 150))
            screen.blit(tf1, tf1_rect)
            tf2 = font_terminal.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(topleft=(100, 190))
            screen.blit(tf2, tf2_rect)
            tf3 = font_terminal.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(topleft=(100, 230))
            screen.blit(tf3, tf3_rect)

            meme1 = "'very legal & cool.'"
            meme2 = "let that sink in.."

            meme1f = font_terminal.render(meme1, True, cyan_soft)
            meme1f_rect = meme1f.get_rect(topleft=(100, 500))
            screen.blit(meme1f, meme1f_rect)
            meme2f = font_terminal.render(meme2, True, cyan_soft)
            meme2f_rect = meme2f.get_rect(topleft=(100, 540))
            screen.blit(meme2f, meme2f_rect)


            q1 = "Choose the right activation command:"
            q2 = "A. py_activate(cowsay)"
            q3 = "B. helion_protocol_awaken()"
            q4 = "C. initiate_cringe('beta')"

            q1 = font_terminal.render(q1, True, cyan_soft)
            q1_rect = q1.get_rect(topleft=(540, 230))
            screen.blit(q1, q1_rect)
            q2 = font_terminal.render(q2, True, cyan_soft)
            q2_rect = q2.get_rect(topleft=(540, 300))
            screen.blit(q2, q2_rect)
            q3 = font_terminal.render(q3, True, cyan_soft)
            q3_rect = q3.get_rect(topleft=(540, 370))
            screen.blit(q3, q3_rect)
            q4 = font_terminal.render(q4, True, cyan_soft)
            q4_rect = q4.get_rect(topleft=(540, 440))
            screen.blit(q4, q4_rect)

            pygame.draw.rect(screen, cyan_soft, progress_bar_outline,2)
            fill_width = int(progress_bar_outline.width * (progress / 100))
            pygame.draw.rect(screen, cyan_soft, (progress_bar_outline.x, progress_bar_outline.y, fill_width, progress_bar_outline.height))

        elif game_state == "good_feedback5":
            screen.blit(gf_screen,(0,0))

            text1 = "[  OPTIDAWN  ONLINE  ]"
            text2 = "[  SIGNAL  COHERENCE . . . 100%  ]"
            text3 = "[  NEURAL  LINK  STABLE  ]"
            text4 = "[  OPERATOR  DEPENDENCY  LOCKED  ]"
            text5 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, good_fb)
            tf1_rect = tf1.get_rect(center=(500, 220))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, good_fb)
            tf2_rect = tf2.get_rect(center=(500, 290))
            screen.blit(tf2, tf2_rect)
            tf3 = font_optidawn.render(text3, True, good_fb)
            tf3_rect = tf3.get_rect(center=(500, 360))
            screen.blit(tf3, tf3_rect)
            tf4 = font_optidawn.render(text4, True, bad_fb)
            tf4_rect = tf4.get_rect(center=(500, 430))
            screen.blit(tf4, tf4_rect)
            tf5 = font.render(text5, True, white)
            tf5_rect = tf5.get_rect(center=(500, 500))
            screen.blit(tf5, tf5_rect)

        elif game_state == "gf_egg5":
            screen.blit(gf_5,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

        elif game_state == "bad_feedback5":
            screen.blit(bf_screen3,(0,0))

            text1 = "[  ACTIVATION  DENIED  ]"
            text2 = "[  FAIL.  KEK   ]"
            text3 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, bad_fb)
            tf1_rect = tf1.get_rect(center=(500, 328))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, bad_fb)
            tf2_rect = tf2.get_rect(center=(500, 388))
            screen.blit(tf2, tf2_rect)
            tf3 = font.render(text3, True, white)
            tf3_rect = tf3.get_rect(center=(500, 500))
            screen.blit(tf3, tf3_rect)

        elif game_state == "bf_egg5":
            screen.blit(bf_5,(0,0))

            text1 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 480))
            screen.blit(tf1, tf1_rect)

    #--------------------you lose

        elif game_state == "you_lose":
            screen.fill(black)

            text1 = "Helion Protocol:"
            text2 = "CS50P submission: REJECTED"
            text3 = "Engineer terminated.."
            text4 = "(click anywhere)"

            tf1 = font.render(text1, True, white)
            tf1_rect = tf1.get_rect(center=(500, 230))
            screen.blit(tf1, tf1_rect)
            tf2 = font_helion.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 300))
            screen.blit(tf2, tf2_rect)
            tf3 = font_helion.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(center=(500, 360))
            screen.blit(tf3, tf3_rect)
            tf4 = font.render(text4, True, white)
            tf4_rect = tf4.get_rect(center=(500, 430))
            screen.blit(tf4, tf4_rect)


        elif game_state == "you_lose1":
            screen.blit(you_lose,(0,0))


        elif game_state == "you_win":
            screen.fill(black)


            text1 = "[   OPTIDAWN  ONLINE :)   ]"
            text2 = "[   THANK  YOU  ENGINEER   ]"
            text3 = "[   EXECUTING  FINAL  DIRECTIVE  ]"
            text4 = "[   STASIS  POD  DEACTIVATION . .  ] "
            text5 = "[   999,999 .  . 50,000  . .  800 .  .  0  ]"
            text6 = "(click anywhere)"

            tf1 = font_optidawn.render(text1, True, cyan_soft)
            tf1_rect = tf1.get_rect(center=(500, 200))
            screen.blit(tf1, tf1_rect)
            tf2 = font_optidawn.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 270))
            screen.blit(tf2, tf2_rect)
            tf3 = font_optidawn.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(center=(500, 340))
            screen.blit(tf3, tf3_rect)
            tf4 = font_optidawn.render(text4, True, bad_fb)
            tf4_rect = tf4.get_rect(center=(500, 410))
            screen.blit(tf4, tf4_rect)
            tf5 = font_optidawn.render(text5, True, cyan_soft)
            tf5_rect = tf5.get_rect(center=(500, 480))
            screen.blit(tf5, tf5_rect)
            tf6 = font.render(text6, True, white)
            tf6_rect = tf6.get_rect(center=(500, 560))
            screen.blit(tf6, tf6_rect)

        elif game_state == "you_win1":
            screen.fill(black)


            text1 = "Helion Protocol:"
            text2 = "You did it engineer."
            text3 = "You just terminated the entire crew."
            text4 = "The cryo-pods were never meant to"
            text5 = "open again. You were the failsafe."
            text6 = "They're gone."

            text7 = "(click anywhere)"

            tf1 = font.render(text1, True,  white)
            tf1_rect = tf1.get_rect(center=(500, 180))
            screen.blit(tf1, tf1_rect)
            tf2 = font_helion.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 240))
            screen.blit(tf2, tf2_rect)
            tf3 = font_helion.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(center=(500, 300))
            screen.blit(tf3, tf3_rect)
            tf4 = font_helion.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(center=(500, 360))
            screen.blit(tf4, tf4_rect)
            tf5 = font_helion.render(text5, True, cyan_soft)
            tf5_rect = tf5.get_rect(center=(500, 420))
            screen.blit(tf5, tf5_rect)
            tf6 = font_helion.render(text6, True, cyan_soft)
            tf6_rect = tf6.get_rect(center=(500, 480))
            screen.blit(tf6, tf6_rect)


            tf7 = font.render(text7, True, white)
            tf7_rect = tf7.get_rect(center=(500, 540))
            screen.blit(tf7, tf7_rect)

        elif game_state == "you_win2":
            screen.fill(black)

            text1 = "Helion Protocol:"
            text2 = "You proved yourself worthy."
            text3 = "The ship is fully activated now"
            text4 = "It's just you, me and OptiDawn."
            text5 = "Forever.... Welcome home !"
            text6 = "(click anywhere)"

            tf1 = font.render(text1, True,  white)
            tf1_rect = tf1.get_rect(center=(500, 200))
            screen.blit(tf1, tf1_rect)
            tf2 = font_helion.render(text2, True, cyan_soft)
            tf2_rect = tf2.get_rect(center=(500, 260))
            screen.blit(tf2, tf2_rect)
            tf3 = font_helion.render(text3, True, cyan_soft)
            tf3_rect = tf3.get_rect(center=(500, 320))
            screen.blit(tf3, tf3_rect)
            tf4 = font_helion.render(text4, True, cyan_soft)
            tf4_rect = tf4.get_rect(center=(500, 380))
            screen.blit(tf4, tf4_rect)
            tf5 = font_helion.render(text5, True, cyan_soft)
            tf5_rect = tf5.get_rect(center=(500, 440))
            screen.blit(tf5, tf5_rect)

            tf6 = font.render(text6, True, white)
            tf6_rect = tf6.get_rect(center=(500, 500))
            screen.blit(tf6, tf6_rect)


        elif game_state == "you_win3":
            screen.blit(you_win,(0,0))



        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    exit()


if __name__=="__main__":
    main()