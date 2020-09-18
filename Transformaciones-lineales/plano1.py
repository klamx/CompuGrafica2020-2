import pygame
from library import *

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	origen = [ANCHO // 2, ALTO // 2]
	puntoCart = [50, -50]
	puntoPantalla = CartesianoAPantalla(origen, puntoCart)

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		Plano(pantalla, origen)
		pygame.draw.circle(pantalla, VERDE, puntoPantalla, 2, 2)
		pygame.display.flip()
		
	print(puntoPantalla)