import os, pygame, sys
from pygame.locals import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/rock.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position [1]
    
    
    def getMoved(self, rocks, direction):
    	old_position = self.rect.topleft
    	other_rocks = pygame.sprite.RenderPlain(rocks)
    	other_rocks.remove(self)
	
    	if direction == "right":
    		self.rect.topleft = self.position[0] + 10, self.position[1]
    	elif direction == "left":
    		self.rect.topleft = self.position[0] - 10, self.position[1]
    	elif direction == "down":
    		self.rect.topleft = self.position[0], self.position[1] +10
    	elif direction == "up":	
    		self.rect.topleft = self.position[0], self.position[1] -10
    		
    	self.position = self.rect.topleft
    	hit_rock = pygame.sprite.spritecollide(self, other_rocks, False)
    	
    	if hit_rock:
    		self.rect.topleft = old_position[0], old_position[1]
    		self.position = old_position


