import pygame
import math
from library import *

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	origen = [ANCHO // 2, ALTO // 2]
	Plano(pantalla, origen)
	x = -50
	

	while x <= 50:
		y = 5*x**3 +10		
		pp = CartesianoAPantalla(origen, [x, y])
		pygame.draw.circle(pantalla, VERDE, pp, 2, 2)
		x += 1
	
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		pygame.display.flip()