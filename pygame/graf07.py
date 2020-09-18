import pygame

ANCHO = 800
ALTO = 600

VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
ROJO = [255, 0, 0]
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
MORADO = [107, 27, 154]

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	fin = False

	pointIndex = 0
	points = [[0, 0], [0, 0]]
	pointList = []

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pointIndex < 6:
					pointList.append(event.pos)
					pygame.draw.circle(pantalla, MORADO, event.pos, 3, 1)
					pointIndex += 1

				if pointIndex == 6:
					pygame.draw.polygon(pantalla, VERDE, pointList, 1)
					pointIndex = 0
					pointList = []

			if event.type == pygame.KEYDOWN:
				pantalla.fill(NEGRO)

		pygame.display.flip()