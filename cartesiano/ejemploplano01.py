import pygame
from library import *

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	origen = [ANCHO // 2, ALTO // 2]
	Plano(pantalla, origen)
	ls = [[100, 100], [-100, 100], [-100, 0]]
	lsCart = [CartesianoAPantalla(origen, ls[0]), CartesianoAPantalla(origen, ls[1]), CartesianoAPantalla(origen, ls[2])]
	pygame.draw.polygon(pantalla, VERDE, lsCart, 1)

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				print event.pos
				pantalla.fill(NEGRO)
				origen = event.pos
				lsCart = [CartesianoAPantalla(origen, ls[0]), CartesianoAPantalla(origen, ls[1]), CartesianoAPantalla(origen, ls[2])]
				Plano(pantalla, event.pos)
				pygame.draw.polygon(pantalla, VERDE, lsCart, 1)

		pygame.display.flip()