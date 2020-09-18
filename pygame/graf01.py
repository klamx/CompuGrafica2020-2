import pygame

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([800, 600])
	
	fin = False
	pos = [0, 0]

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				print (event.pos, event.button)
				pos = event.pos

		pygame.draw.line(pantalla, (0, 255, 0), [0, 0], pos, 2)
		pygame.display.flip()