import pygame
from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False

	ls = [[20, 80], [100, 80]]
	T = [-28, 80]
	lsE = []

	# trasladar al origen
	for p in ls:
		pt = escalapf(T, p, 2)
		lsE.append(pt)

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		pygame.draw.line(pantalla, BLANCO, lsE[0], lsE[1], 2)
		pygame.draw.line(pantalla, VERDE, ls[0], ls[1], 2)
		pygame.display.flip()
