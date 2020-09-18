import pygame
from library import *

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	origen = [ANCHO // 2, ALTO // 2]
	ls = [[100, 100], [100, 300], [300, 100]]
	lsCart = []
	for x in  ls:
		pCart = CartesianoAPantalla(origen, x)
		lsCart.append(pCart)

	lsNew = []

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					pygame.draw.polygon(pantalla, VERDE, lsCart, 1)

				if event.key == pygame.K_2:
					lsNew = []
					for x in ls:
						x[0] = x[0] - 400
						pCart = CartesianoAPantalla(origen, x)
						lsNew.append(pCart)
					pygame.draw.polygon(pantalla, VERDE, lsNew, 1)

				if event.key == pygame.K_3:
					lsNew = []
					for x in lsCart:
						x[0] = x[0] * -1
						lsNew.append(x)
					pygame.draw.polygon(pantalla, MORADO, lsNew, 1)

				if event.key == pygame.K_4:
					lsNew = []
					for x in lsCart:
						x[0] = x[0] * -1
						lsNew.append(x)			
					pygame.draw.polygon(pantalla, VERDE, lsNew, 1)	

		Plano(pantalla, origen)

		pygame.display.flip()
