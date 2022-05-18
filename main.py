#imports
import pygame
import time
import story

#open pygame
pygame.init()
X = 700
Y = 500
display_surface = pygame.display.set_mode((X, Y))

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (54, 246, 124)
lightgreen = (0, 242, 65)
RED = (255, 51, 51)

#tuples
timetake = (20, 20)
monsters = ("fire monster", "grass monster")
hps = (50, 70)
monsterasset = ('assets/monsters/fire_monster.png', 'assets/monsters/grass_monster.png')
textcolor = (BLACK, WHITE)
completecolor = (lightgreen, lightgreen)

#variables!
#size
size = (700, 500)

#done?
done = False

#the level variable
level = 0

#clickednumber
clicked = 0

#fps constant
clock = pygame.time.Clock()

#timer function
first = time.time() + timetake[level]
second = time.time()

#fonts
freesansbold = pygame.font.Font('freesansbold.ttf', 32)
smallfreesansbold = pygame.font.Font('freesansbold.ttf', 32)

#functions
def colorcounter(text):
    #imports
    global level
    global hps
    #colors
    global BLACK
    global WHITE
    global lightgreen
    global RED
    if text == "COMPLETE" or text >= hps[level]:
        return freesansbold.render(f"{text}", True, completecolor[level])
    else:
        return freesansbold.render(f"{text}/{hps[level]}", True,
                                   textcolor[level])


#declare visual stuff

#the counter text
counter = colorcounter(clicked)
textRect = counter.get_rect()
textRect.center = (X // 2, 450)

#the clicking image
image = pygame.image.load(monsterasset[level])
imgRect = image.get_rect()
imgRect.center = (X // 2, Y // 2)

#discription text
dscrpt = smallfreesansbold.render(
    f"click the {monsters[level]}. you have {round(first - second)} seconds",
    True, BLACK)
rect2 = dscrpt.get_rect()

#display
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clicker rpg")

#program
while not done:
    #load changing text/image
    dscrpt = freesansbold.render(
        f"click the {monsters[level]}. you have {round(first - second)} seconds",
        True, BLACK)
    if clicked >= hps[level]:
        screen.fill(WHITE)
        counter = colorcounter("COMPLETE")
        textRect = counter.get_rect()
        textRect.center = (X // 2, 450)
        display_surface.blit(counter, textRect)
        pygame.display.flip()
        time.sleep(5)
        clicked = 0
        level += 1
        image = pygame.image.load(monsterasset[level])
        imgRect = image.get_rect()
        imgRect.center = (X // 2, Y // 2)
        counter = colorcounter(clicked)
        textRect = counter.get_rect()
        textRect.center = (X // 2, 450)
        display_surface.blit(counter, textRect)
        pygame.display.flip()
    else:
        counter = colorcounter(clicked)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if imgRect.collidepoint(pygame.mouse.get_pos(
        )) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked += 1
    #logic
    second = time.time()
    if second > first:
        clicked = 0
        first = time.time() + timetake[level]
    #background
    screen.fill(WHITE)

    #visualizer
    display_surface.blit(image, imgRect)
    display_surface.blit(counter, textRect)
    display_surface.blit(dscrpt, rect2)

    #screenupdate
    pygame.display.flip()

    # fps
    clock.tick(60)

# Close the window and quit.
pygame.quit()
