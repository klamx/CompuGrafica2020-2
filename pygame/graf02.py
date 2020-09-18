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

			if event.type == pygame.MOUSEMOTION:
				pos = event.pos

		pantalla.fill((0, 0, 0))
		pygame.draw.circle(pantalla, (0, 255, 0), pos, 50, 1)
		pygame.display.flip()