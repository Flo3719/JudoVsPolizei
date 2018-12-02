import sys, pygame
pygame.init()
size = width, height = 640, 512
speed = (int(5), int(0))
#               R       G       B       A
black =         255,    255,    255,    0
green =         0,      255,    0,      0
red =           255,    0,      0,      0
yellow =        255,    255,    0,      0
grey =          100,    100,    100,    0

gameDisplay = pygame.display.set_mode((640, 512))

pygame.display.set_caption("JUDO VS POLIZEI")
icon = pygame.image.load("UI/icon.png")
pygame.display.set_icon (icon)
screen = pygame.display.set_mode(size)
pygame.display.toggle_fullscreen
waitscreen = pygame.image.load ("UI/startscreen.png")
screen.blit (waitscreen, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
startgame = pygame.image.load("UI/startgame.png")
options = pygame.image.load("UI/Anleitung.png")
endgame = pygame.image.load("UI/endgame.png")
zurueck = pygame.image.load("UI/back.png")
anleitungtext = pygame.image.load("UI/AnleitungText.png")
cursorsprite = pygame.image.load("GFX/jwalk2.png")
atkklein = pygame.image.load("GFX/jatk.png")
cursorsprite = pygame.image.load("GFX/pwalk2.png")
atkklein = pygame.image.load("GFX/patk.png")
cursorspritef = pygame.transform.flip(cursorsprite, 1, 0)
atkkleinf = pygame.transform.flip(atkklein, 1, 0)
menuebackground = pygame.image.load("GFX/city_stage.png")

#Musik
#pygame.mixer.init()                             #Mixer Laden
#pygame.mixer.music.load("whatislove.mp3")      #Ld Musik
musicplays = False

#Sounds
#sound_countdown=pygame.mixer.Sound("countdown.wav")
#sound_countdown_end=pygame.mixer.Sound("countdown_end.wav")
#sound_judo_hit=pygame.mixer.Sound("police_hit.wav")
#sound_judo_jump=pygame.mixer.Sound("judo_jump.wav")
#sound_no_hit=pygame.mixer.Sound("no_hit.wav")
#sound_police_hit=pygame.mixer.Sound("police_hit.wav")
#sound_police_jump=pygame.mixer.Sound("police_jump.wav")
#sound_select=pygame.mixer.Sound("select.wav")

#Stages
citystage_background = pygame.image.load("GFX/city_stage.png")
foreststage_background = pygame.image.load("GFX/forest_stage.png")
stage3_background = pygame.image.load("GFX/stage3.png")

stagebackground = foreststage_background

#winscreen

winscreen_background = pygame.image.load("UI/winscreen.png")

ja_button = pygame.image.load("UI/ja_button.png")
nein_button = pygame.image.load("UI/nein_button.png")

winscreen_auswahl = 1

#Flos Shit

startgame = pygame.image.load("UI/startgame.png")
options = pygame.image.load("UI/Anleitung.png")
endgame = pygame.image.load("UI/endgame.png")
zurueck = pygame.image.load("UI/back.png")

titelschrift = pygame.image.load("UI/title.png")

#stageauswahl

citystage_button = pygame.image.load("UI/city_stage_button.png")
foreststage_button = pygame.image.load("UI/forest_stage_button.png")
stage3_button = pygame.image.load("UI/stage3_stage_button.png")

stagemenueauswahl = 1
menueauswahl = 1

wo = "menue"

class j:
        cursorsprite = pygame.image.load("GFX/jwalk2.png")
        atkklein = pygame.image.load("GFX/jatkklein.png")
        health  =   100
        walk1   =       pygame.image.load("GFX/jwalk1groß2.png")
        walk2   =       pygame.image.load("GFX/jwalk2groß2.png")
        walk3   =       pygame.image.load("GFX/jwalk3groß2.png")
        atk     =       pygame.image.load ("GFX/jatkgroß.png")
        walk1f  =       pygame.transform.flip(walk1, 1, 0)
        walk2f  =       pygame.transform.flip(walk2, 1, 0)
        walk3f  =       pygame.transform.flip(walk3, 1, 0)
        atkf    =       pygame.transform.flip (atk, 1, 0)
        walkr   =       walk1.get_rect()
        walk    =       1
        jump    =       False
        jumpcount =     0
        direction =     False
#      walkr   =       walkr.move(0, 370)
        walkr.x = 0
        walkr.y
        hitscan =       False

        global wo


        @staticmethod
        def move ():
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                pygame.event.pump()
                key = pygame.key.get_pressed()
                if key[pygame.K_w] or key[pygame.K_v]:
                        j.jump = True
                if j.jump == True:
                        if key[pygame.K_a] and not j.walkr.left< 0:
                                j.walkr = j.walkr.move (-speed[0], speed[1])
                                j.direction = True
                        if key[pygame.K_d] and not j.walkr.right > width:
                                j.walkr = j.walkr.move (speed[0], speed[1])
                                j.direction = False
                else:
                        if key[pygame.K_a] and not j.walkr.left< 0:
                                if key[pygame.K_c]:
                                        j.direction = True
                                else:
                                        j.walkr = j.walkr.move (-speed[0], speed[1])
                                        j.direction = True
                        if key[pygame.K_d] and not j.walkr.right > width:
                                if key[pygame.K_c]:
                                        j.direction = False
                                else:
                                        j.walkr = j.walkr.move (speed[0], speed[1])
                                        j.direction = False
                        if wo == "citystage":
                                if j.walkr.bottom < 345:
                                        j.walkr = j.walkr.move(speed[1], speed[0])
                        if wo == "foreststage":
                                if j.walkr.bottom < 505:
                                        j.walkr = j.walkr.move(speed[1], speed[0])
                        if wo == "stage3":
                                if j.walkr.bottom < 430:
                                        j.walkr = j.walkr.move(speed[1], speed[0])
        @staticmethod
        def jmp():
                if j.jumpcount < 20:
                        j.jumpcount = j.jumpcount + 1
                        j.walkr = j.walkr.move (speed[1], -speed[0])
                elif j.jumpcount >= 20 and j.jumpcount < 40:
                        j.walkr = j.walkr.move (speed[1], speed[0])
                        j.jumpcount = j.jumpcount + 1
                elif j.jumpcount >= 40:
                        j.jumpcount = 0
                        j.jump = False
        @staticmethod
        def draw():
                pygame.event.pump()
                key = pygame.key.get_pressed()
                if  key[pygame.K_a] and j.jump == False:
                        if key[pygame.K_c]:
                                screen.blit(j.atkf, j.walkr)
                        else:
                                if j.walk >= 1 and j.walk <= 3:
                                        screen.blit(j.walk1f, j.walkr)
                                if j.walk >= 4 and j.walk <= 6:
                                        screen.blit(j.walk2f, j.walkr)
                                if j.walk >= 7 and j.walk <= 9:
                                        screen.blit(j.walk3f, j.walkr)
                                j.walk = j.walk + 1
                                if j.walk > 9:
                                        j.walk = 1
                elif  key[pygame.K_d] and j.jump == False:
                        if key[pygame.K_c]:
                                screen.blit(j.atk, j.walkr)
                        else:
                                if j.walk >= 1 and j.walk <= 3:
                                        screen.blit(j.walk1, j.walkr)
                                if j.walk >= 4 and j.walk <= 6:
                                        screen.blit(j.walk2, j.walkr)
                                if j.walk >= 7 and j.walk <= 9:
                                        screen.blit(j.walk3, j.walkr)
                                j.walk = j.walk + 1
                                if j.walk > 9:
                                        j.walk = 1
                elif j.jump == True :
                        if key[pygame.K_d]:
                                if key[pygame.K_c]:
                                        screen.blit(j.atk, j.walkr)
                                else:
                                        screen.blit(j.walk1, j.walkr)
                        elif key[pygame.K_a]:
                                if key[pygame.K_c]:
                                        screen.blit(j.atkf, j.walkr)
                                else:
                                        screen.blit(j.walk1f, j.walkr)
                        else:
                                if j.direction == True:
                                        if key[pygame.K_c]:
                                                screen.blit (j.atkf, j.walkr)
                                        else:
                                                screen.blit(j.walk1f, j.walkr)
                                else:
                                        if key[pygame.K_c]:
                                                screen.blit (j.atk, j.walkr)
                                        else:
                                                screen.blit(j.walk1, j.walkr)
                else:
                        if j.direction == True:
                                if key[pygame.K_c]:
                                        screen.blit (j.atkf, j.walkr)
                                else:
                                        screen.blit(j.walk2f, j.walkr)
                        else:
                                if key[pygame.K_c]:
                                        screen.blit(j.atk, j.walkr)
                                else:
                                                screen.blit(j.walk2, j.walkr)
        @staticmethod
        def hiscan():
                if j.walkr.colliderect(p.walkr):
                        if j.direction == True and j.walkr.left > p.walkr.left:
                                j.hitscan = True
                        elif j.direction == False and j.walkr.right < p.walkr.right:
                                j.hitscan = True
                        else:
                                j.hitscan = False
                else:
                        j.hitscan = False
class p:
        cursorsprite = pygame.image.load("GFX/pwalk2.png")
        atkklein = pygame.image.load("GFX/patkklein.png")
        cursorspritef = pygame.transform.flip(cursorsprite, 1, 0)
        atkkleinf = pygame.transform.flip(atkklein, 1, 0)
        health  =   100
        walk1   =       pygame.image.load("GFX/pwalk1groß.png")
        walk2   =       pygame.image.load("GFX/pwalk2groß.png")
        walk3   =       pygame.image.load("GFX/pwalk3groß.png")
        atk     =       pygame.image.load("GFX/patkgroß.png")
        walk1f  =       pygame.transform.flip(walk1, 1, 0)
        walk2f  =       pygame.transform.flip(walk2, 1, 0)
        walk3f  =       pygame.transform.flip(walk3, 1, 0)
        atkf    =       pygame.transform.flip(atk, 1, 0)
        walkr   =       walk1.get_rect()
        walk    =       1
        jump    =       False
        jumpcount =     0
        direction =     True #true = links, false = rechts
        hitscan =       False
#        walkr.x = 550
#        walkr.y

        global stagebackground
        global citystage_background
        global foreststage_background
        global stage3_background

        @staticmethod
        def move ():

                global stagebackground
                global citystage_background
                global foreststage_background
                global stage3_background

                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                pygame.event.pump()
                key = pygame.key.get_pressed()
                if key[pygame.K_UP] or key[pygame.K_PERIOD]:
                        p.jump = True
                if p.jump == True:
                        if key[pygame.K_LEFT] and not p.walkr.left< 0:
                                p.walkr = p.walkr.move (-speed[0], speed[1])
                                p.direction = False
                        if key[pygame.K_RIGHT] and not p.walkr.right > width:
                                p.walkr = p.walkr.move (speed[0], speed[1])
                                p.direction = True
                else:
                        if key[pygame.K_LEFT] and not p.walkr.left< 0:
                                if key[pygame.K_COMMA]:
                                        p.direction = False
                                else:
                                        p.walkr = p.walkr.move (-speed[0], speed[1])
                                        p.direction = False
                        if key[pygame.K_RIGHT] and not p.walkr.right > width:
                                if key[pygame.K_COMMA]:
                                        p.direction = True
                                else:
                                        p.walkr = p.walkr.move (speed[0], speed[1])
                                        p.direction = True
                        if wo == "citystage":
                                if p.walkr.bottom < 345:
                                        p.walkr = p.walkr.move(speed[1], speed[0])
                        if wo == "foreststage":
                                if p.walkr.bottom < 505:
                                        p.walkr = p.walkr.move(speed[1], speed[0])
                        if wo == "stage3":
                                if p.walkr.bottom < 430:
                                        p.walkr = p.walkr.move(speed[1], speed[0])
        @staticmethod
        def jmp():
                if p.jumpcount < 20:
                        p.jumpcount = p.jumpcount + 1
                        p.walkr = p.walkr.move (speed[1], -speed[0])
                elif p.jumpcount >= 20 and p.jumpcount < 40:
                        p.walkr = p.walkr.move (speed[1], speed[0])
                        p.jumpcount = p.jumpcount + 1
                elif p.jumpcount >= 40:
                        p.jumpcount = 0
                        p.jump = False



        @staticmethod
        def draw():
                pygame.event.pump()
                key = pygame.key.get_pressed()
                if  key[pygame.K_LEFT] and p.jump == False:
                        if key[pygame.K_COMMA]:
                                screen.blit(p.atk, p.walkr)
                        else:
                                if p.walk >= 1 and p.walk <= 3:
                                        screen.blit(p.walk1, p.walkr)
                                if p.walk >= 4 and p.walk <= 6:
                                        screen.blit(p.walk2, p.walkr)
                                if p.walk >= 7 and p.walk <= 9:
                                        screen.blit(p.walk3, p.walkr)
                                p.walk = p.walk + 1
                                if p.walk > 9:
                                        p.walk = 1
                elif  key[pygame.K_RIGHT] and p.jump == False:
                        if key[pygame.K_COMMA]:
                                screen.blit(p.atkf, p.walkr)
                        else:
                                if p.walk >= 1 and p.walk <= 3:
                                        screen.blit(p.walk1f, p.walkr)
                                if p.walk >= 4 and p.walk <= 6:
                                        screen.blit(p.walk2f, p.walkr)
                                if p.walk >= 7 and p.walk <= 9:
                                        screen.blit(p.walk3f, p.walkr)
                                p.walk = p.walk + 1
                                if p.walk > 9:
                                        p.walk = 1
                elif p.jump == True :
                        if key[pygame.K_RIGHT]:
                                if key[pygame.K_COMMA]:
                                        screen.blit(p.atkf, p.walkr)
                                else:
                                        screen.blit(p.walk1f, p.walkr)
                        elif key[pygame.K_LEFT]:
                                if key[pygame.K_COMMA]:
                                        screen.blit(p.atk, p.walkr)
                                else:
                                        screen.blit(p.walk1, p.walkr)
                        else:
                                if p.direction == True:
                                        if key[pygame.K_COMMA]:
                                                screen.blit (p.atkf, p.walkr)
                                        else:
                                                screen.blit(p.walk1f, p.walkr)
                                else:
                                        if key[pygame.K_COMMA]:
                                                screen.blit (p.atk, p.walkr)
                                        else:
                                                screen.blit(p.walk1, p.walkr)
                else:
                        if p.direction == False:
                                if key[pygame.K_COMMA]:
                                        screen.blit (p.atk, p.walkr)
                                else:
                                        screen.blit(p.walk2, p.walkr)
                        else:
                                if key[pygame.K_COMMA]:
                                        screen.blit(p.atkf, p.walkr)
                                else:
                                        screen.blit(p.walk2f, p.walkr)
        @staticmethod
        def hiscan():
                if  p.walkr.colliderect(j.walkr):
                        if p.direction == True and p.walkr.left < j.walkr.left:
                                p.hitscan = True
                        elif p.direction == False and p.walkr.right > j.walkr.right:
                                p.hitscan = True
                        else:
                                p.hitscan = False
                else:
                        p.hitscan = False




def winscreen(winner):
        global wo
        global winscreen_auswahl
        wo = "winscreen"

        screen.blit(winscreen_background, (0,0))
        screen.blit(nein_button, (220,452))
        screen.blit(ja_button, (220, 372))

        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and winscreen_auswahl == 1:
             #pygame.mixer.Sound.play(sound_select)
             winscreen_auswahl = winscreen_auswahl + 1
             pygame.time.wait(150)
        if key[pygame.K_UP] and winscreen_auswahl == 2:
             #pygame.mixer.Sound.play(sound_select)
             winscreen_auswahl = winscreen_auswahl - 1
             pygame.time.wait(150)

        if winscreen_auswahl == 1:
                if key[pygame.K_RETURN]:
                        screen.blit(j.atkklein, (190, 352))
                        screen.blit(p.atkkleinf, (417, 352))
                        startapp()
                else:
                        screen.blit(j.cursorsprite, (190, 352))
                screen.blit(p.cursorspritef, (417, 352))

        if winscreen_auswahl == 2:
                if key[pygame.K_RETURN]:
                       screen.blit(j.atkklein, (190, 432))
                       screen.blit(p.atkkleinf, (417, 432))
                       startapp()
                else:
                        screen.blit(j.cursorsprite, (190, 432))
                        screen.blit(p.cursorspritef, (417, 432))

        if winner == "Judokämpfer":
                screen.blit(j.walk1, (298,20))
        else:
                screen.blit(p.walk1, (298,20))

def countdown(stagebackground):

        global musicplays

        musicplays = False
        music()

        p.health = 100
        j.health = 100

        p.walkr.x = 550
        j.walkr.x = 0
        if stagebackground == stage3_background:
                p.walkr.y = 310
                j.walkr.y = 310
        if stagebackground == citystage_background:
                p.walkr.y = 345
                j.walkr.y = 345
        if stagebackground == foreststage_background:
                p.walkr.y = 350
                j.walkr.y = 350


        j.direction = False
        j.jump  = False

        p.direction = False
        p.jump  = False

        countdown_3 = pygame.image.load("UI/countdown_3.png")
        countdown_2 = pygame.image.load("UI/countdown_2.png")
        countdown_1 = pygame.image.load("UI/countdown_1.png")
        countdown_0 = pygame.image.load("UI/countdown_0.png")

        screen.blit(stagebackground, (0, 0))
        p.draw()
        j.draw()

        screen.blit(stagebackground, (0, 0))
        p.draw()
        j.draw()
        screen.blit(countdown_3, (0,0))
        #pygame.mixer.Sound.play(sound_countdown)
        pygame.display.flip()
        pygame.time.wait(1000)

        screen.blit(stagebackground, (0, 0))
        p.draw()
        j.draw()
        screen.blit(countdown_2, (0,0))
        #pygame.mixer.Sound.play(sound_countdown)
        pygame.display.flip()
        pygame.time.wait(1000)

        screen.blit(stagebackground, (0, 0))
        p.draw()
        j.draw()
        screen.blit(countdown_1, (0,0))
        #pygame.mixer.Sound.play(sound_countdown)
        pygame.display.flip()
        pygame.time.wait(1000)

        screen.blit(stagebackground, (0, 0))
        p.draw()
        j.draw()
        screen.blit(countdown_0, (0,0))
        #pygame.mixer.Sound.play(sound_countdown_end)
        pygame.display.flip()
        pygame.time.wait(1000)

        game(clock, stagebackground)

def hp_bar(p_health, j_health):

    if p_health > 75:
        p_health_color = green
    elif p_health > 50:
        p_health_color = yellow
    else:
        p_health_color = red

    if j_health > 75:
        j_health_color = green
    elif j_health > 50:
        j_health_color = yellow
    else:
        j_health_color = red

    pygame.draw.rect(gameDisplay, grey, (10, 10, 200, 25))
    pygame.draw.rect(gameDisplay, grey, (430, 10, 200, 25))

    pygame.draw.rect(gameDisplay, j_health_color, (10, 10, j_health*2, 25))
    pygame.draw.rect(gameDisplay, p_health_color, (430, 10, p_health*2, 25))

def game(clock,stagebackground):
    while 1:

        screen.blit(stagebackground, (0, 0))

        j.move ()
        if j.jump == True:
                j.jmp ()

        p.move ()
        if p.jump == True:
                p.jmp ()

        p.draw()
        j.draw()
        hit()

        hp_bar(p.health, j.health)

        pygame.display.flip()
        screen.fill(black)

        clock.tick(60)

def music():

        global musicplays

        if wo=="menue" or wo=="stageauswahl" or wo=="anleitung" or wo=="winscreen" and musicplays == False:
                musicplays = True
                #pygame.mixer.music.play(-1)                     #Spielt Musik endlos(-1 .bergeben)
        elif    musicplays == True:
                musicplays = True

        elif wo=="citystage" or wo=="foreststage" or wo=="stage3":
                musicplays = False
                #pygame.mixer.music.stop()

def hit():
        global wo
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if wo == "citystage" or "foreststage" or "stage3":
                if key[pygame.K_c]:
                        j.hiscan()
                        if j.hitscan == True and p.health > 0:
                                #pygame.mixer.Sound.play(sound_judo_hit)
                                p.health = p.health - 1
                                print (p.health)
                if key[pygame.K_COMMA]:
                        p.hiscan()
                        if p.hitscan == True and j.health > 0:
                                #pygame.mixer.Sound.play(sound_police_hit)
                                j.health = j.health - 1
                                print (j.health)
                if p.health <= 0:
                        winner = "Judokämpfer"
                        wo = "winscreen"
                        winscreen(winner)
                if j.health <= 0:
                        winner = "Polizist"
                        wo = "winscreen"
                        winscreen(winner)
def menue():

        global menueauswahl
        global wo

        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and menueauswahl < 3:
             #pygame.mixer.Sound.play(sound_select)
             menueauswahl = menueauswahl + 1
             pygame.time.wait(150)
        if key[pygame.K_UP] and menueauswahl > 1:
             #pygame.mixer.Sound.play(sound_select)
             menueauswahl = menueauswahl - 1
             pygame.time.wait(150)

        screen.fill(black)
        screen.blit(menuebackground, (0,0))

        screen.blit(titelschrift, (120, 0))

        screen.blit(startgame, (220,100))
        screen.blit(options, (220,200))
        screen.blit(endgame, (220,300))

        if menueauswahl == 1:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 80))
                screen.blit(p.atkkleinf, (417, 80))
            else:
                screen.blit(j.cursorsprite, (190, 80))
                screen.blit(p.cursorspritef, (417, 80))
        if menueauswahl == 2:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 180))
                screen.blit(p.atkkleinf, (417, 180))
            else:
                screen.blit(j.cursorsprite, (190, 180))
                screen.blit(p.cursorspritef, (417, 180))
        if menueauswahl == 3:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 280))
                screen.blit(p.atkkleinf, (417, 280))
            else:
                screen.blit(j.cursorsprite, (190, 280))
                screen.blit(p.cursorspritef, (417, 280))

        if key[pygame.K_RETURN] and menueauswahl == 3:
            quit()

def anleitung():

        pygame.event.pump()
        key = pygame.key.get_pressed()

        screen.blit(menuebackground, (0,0))
        screen.blit(options, (220, 10))
        screen.blit(zurueck, (220,452))

        screen.blit(anleitungtext, (10, 70))

        if key[pygame.K_RETURN]:
            screen.blit(j.atkklein, (190, 432))
            screen.blit(p.atkkleinf, (417, 432))
        else:
            screen.blit(j.cursorsprite, (190, 432))
            screen.blit(p.cursorspritef, (417, 432))

def startapp ():

   global musicplays
   music()

   while 1:
                global stagemenueauswahl
                global wo
                global citystage_background
                global foreststage_background
                global stage3_background
                global winscreen_auswahl

                if wo == "anleitung":
                    anleitung()
                    pygame.display.flip()
                else:
                    if wo == "menue":
                        menue()
                        pygame.display.flip()

                    else:
                        stageauswahl()
                        pygame.display.flip()


#STAGES
                if wo == "citystage":
                        stagebackground = citystage_background
                        countdown(stagebackground)

                if wo == "foreststage":
                        stagebackground = foreststage_background
                        countdown(stagebackground)

                if wo == "stage3":
                        stagebackground = stage3_background
                        countdown(stagebackground)
#MENue

                if[pygame.K_RETURN] and menueauswahl == 2 and wo == "menue":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "anleitung"

                if[pygame.K_RETURN] and menueauswahl == 1 and wo == "menue":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "stageauswahl"

#ANLEITUNG

                if[pygame.K_RETURN] and wo == "anleitung":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "menue"

#STAGEAUSWAHL
                if[pygame.K_RETURN] and stagemenueauswahl == 4 and wo == "stageauswahl":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "menue"


                if[pygame.K_RETURN] and stagemenueauswahl == 1 and wo == "stageauswahl":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "citystage"
                                music()

                if[pygame.K_RETURN] and stagemenueauswahl == 2 and wo == "stageauswahl":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "foreststage"
                                music()

                if[pygame.K_RETURN] and stagemenueauswahl == 3 and wo == "stageauswahl":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "stage3"
                                music()

#WINSCREEN
                if[pygame.K_RETURN] and winscreen_auswahl == 1 and wo == "winscreen":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "stageauswahl"

                if[pygame.K_RETURN] and winscreen_auswahl == 2 and wo == "winscreen":
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RETURN:
                                wo = "menue"
                                music()

def stageauswahl():

    global citystage_button

    global foreststage_button

    global stage3_button

    global stagewahl_titel

    global stagemenueauswahl

    screen.fill(black)
    screen.blit(menuebackground, (0,0))

    screen.blit(titelschrift, (120, 0))

    screen.blit(citystage_button, (220,100))
    screen.blit(foreststage_button, (220,200))
    screen.blit(stage3_button, (220,300))
    screen.blit(zurueck, (220,452))

    pygame.event.pump()
    key = pygame.key.get_pressed()

    if wo == "stageauswahl":
        if key[pygame.K_DOWN] and stagemenueauswahl < 4:
            #pygame.mixer.Sound.play(sound_select)
            stagemenueauswahl = stagemenueauswahl + 1
            pygame.time.wait(150)
        if key[pygame.K_UP] and stagemenueauswahl > 1:
            #pygame.mixer.Sound.play(sound_select)
            stagemenueauswahl = stagemenueauswahl - 1
            pygame.time.wait(150)

            screen.fill(black)
            screen.blit(menuebackground, (0,0))

            screen.blit(titelschrift, (120, 0))

            screen.blit(citystage_button, (220,100))
            screen.blit(foreststage_button, (220,200))
            screen.blit(stage3_button, (220,300))
            screen.blit(zurueck, (220,452))

    if stagemenueauswahl == 1:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 80))
                screen.blit(p.atkkleinf, (417, 80))
            else:
                screen.blit(j.cursorsprite, (190, 80))
                screen.blit(p.cursorspritef, (417, 80))
    if stagemenueauswahl == 2:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 180))
                screen.blit(p.atkkleinf, (417, 180))
            else:
                screen.blit(j.cursorsprite, (190, 180))
                screen.blit(p.cursorspritef, (417, 180))
    if stagemenueauswahl == 3:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 280))
                screen.blit(p.atkkleinf, (417, 280))
            else:
                screen.blit(j.cursorsprite, (190, 280))
                screen.blit(p.cursorspritef, (417, 280))
    if stagemenueauswahl == 4:
            if key[pygame.K_RETURN]:
                screen.blit(j.atkklein, (190, 432))
                screen.blit(p.atkkleinf, (417, 432))
            else:
                screen.blit(j.cursorsprite, (190, 432))
                screen.blit(p.cursorspritef, (417, 432))

while 1:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                startapp()
        if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
