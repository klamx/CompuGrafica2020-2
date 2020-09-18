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
	pointList = []
	vel_x = 0
	vel_y = 0
	color = BLANCO
	reloj = pygame.time.Clock()

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pointIndex < 3:
					pointList.append(list(event.pos))
					pygame.draw.circle(pantalla, BLANCO, event.pos, 3, 2)
					pointIndex += 1

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pointIndex = 0
					pointList = []
					vel_x = 0
					color = BLANCO
					pantalla.fill(NEGRO)

				if event.key == pygame.K_RIGHT:
					vel_x = 8
					vel_y = 0
					color = VERDE

				if event.key == pygame.K_LEFT:
					vel_x = -8
					vel_y = 0
					color = MORADO

				if event.key == pygame.K_DOWN:
					vel_y = 8
					vel_x = 0
					color = VERDE

				if event.key == pygame.K_UP:
					vel_y = -8
					vel_x = 0
					color = MORADO

		for p in pointList:
			p[0] += vel_x
			p[1] += vel_y

		# pantalla.fill(NEGRO)
		if pointIndex == 3:
			pygame.draw.polygon(pantalla, color, pointList, 1)
		pygame.display.flip()
		reloj.tick(60)