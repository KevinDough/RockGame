#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *
from doors import Door
from player import Player
from rocks import Rock
from levels import Levels
from HUB import HUB

pygame.init()




WIDTH = 675
HEIGHT = 500
"Window 675 x 500"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
x = WIDTH / 2
y = HEIGHT / 2
# new_position = (x,y)


player = Player((x,y))
playerGroup = pygame.sprite.RenderPlain(player)
HUB = HUB()


rocks_by_level = Levels().createLevels_Rock()
doors_by_level = Levels().createLevels_Door()
enemies_by_level = Levels().createLevels_enemies(windowSurface)

WHITE = pygame.Color(255,255,255) #Temp background
fpsClock = pygame.time.Clock()

current_level =0
pygame.key.set_repeat(1, 10)
while True:
    windowSurface.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
    

    
    levelChange = pygame.sprite.spritecollide(player, doors_by_level[current_level],True)
    
    if levelChange:
        current_level = 1
        player.getBelt()

    player.update_position(rocks_by_level[current_level], playerGroup, enemies_by_level[current_level])
    playerGroup.draw(windowSurface)
    enemies_by_level[current_level].draw(windowSurface)
    enemies_by_level[current_level].update(player, rocks_by_level[current_level])
    doors_by_level[current_level].draw(windowSurface)
    rocks_by_level[current_level].draw(windowSurface)
    HUB.drawHealth(player, windowSurface)
    pygame.display.update()
    fpsClock.tick(30)
    
