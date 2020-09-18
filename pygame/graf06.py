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
				# pointList.append(event.pos)
				if pointIndex < 2:
					if pointIndex == 0:
						points[pointIndex] = (event.pos)
						pointIndex += 1

					if pointIndex == 1:
						points[pointIndex] = (event.pos)
						pygame.draw.line(pantalla, VERDE, points[0], points[1])
						points[0], points[1] = points[1], points[0]

		pygame.display.flip()

	pygame.quit()
	# print('Puntos marcados en la pantalla: ', pointList)
	# print('Cantidad de puntos: ', len(pointList))