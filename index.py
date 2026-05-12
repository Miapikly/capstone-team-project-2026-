import pygame
import spritesheet

pygame.init()
screen = pygame.display.set_mode((1280,720))

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = [4,6,3,4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown=500
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(0,24,24,3,BLACK))

run = True
while run:

	#update background
	screen.fill(BG)

    #update animation
current_time = pygame.time.get_ticks()
if current_time-last_update>=animation_cooldown:
    frame += 1
    last_update = current_time
if frame >= len(animation_list):
		frame=0


	#show frame image
screen.blit(animation_list[frame], (0,0))

	#event handler
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		run = False
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_DOWN and action >0:
            action -= 1
            frame = 1

pygame.display.update()

pygame.quit()