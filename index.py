import pygame
from pygame.locals import *
import sys
import spritesheet
from dialogue import DialogBox

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BG = (50, 50, 50)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

x = (pygame.display.get_surface().get_width() // 2) - 250
y = pygame.display.get_surface().get_height() - 250

def run(self):
		while True:

			self.dialog = "* Hello World\n* Test"
			self.dialogbox = DialogBox(x, y, 500, 250, self.dialog)

			sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
			sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

			animation_list = []
			animation_steps = [4,6,3,4]
			action = 0
			last_update = pygame.time.get_ticks()
			animation_cooldown=250
			frame = 0
			step_counter = 0

			#update animation
			current_time = pygame.time.get_ticks()
			if current_time-last_update>=animation_cooldown:
				frame += 1
				last_update = current_time
				if frame >= len(animation_list[action]):
					frame=0

			#show frame image
			self.screen.blit(animation_list[action][frame], (0,0))



			for animation in animation_steps:
				temp_img_list = []
			for _ in range(animation):
				temp_img_list.append(sprite_sheet.get_image(step_counter,40,70,1,BLACK))
				step_counter += 1
				animation_list.append(temp_img_list)



			#event handler
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN and action >0:
						action += 1
						frame = 0
					if event.key == pygame.K_UP and action < len(animation_list) -1:
						action +=1
						frame = 0
				#self.screen.fill("purple")
				run(self)
				self.dialogbox.render()

pygame.display.update()





