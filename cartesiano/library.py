import pygame

ANCHO = 800
ALTO = 600

VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
ROJO = [255, 0, 0]
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
MORADO = [107, 27, 154]

# Dibuja un plano carteciano
def Plano(pantalla, origen, color = BLANCO, d = 1):
	ox = origen[0]
	oy = origen[1]
	pygame.draw.line(pantalla, color, [0, oy], [ANCHO, oy], d)
	pygame.draw.line(pantalla, color, [ox, 0], [ox, ALTO], d)

def CartesianoAPantalla(origen, punto):
	px = punto[0] + origen[0]
	py = origen[1] - punto[1]
	return [px, py]

def Punto(pantalla, punto, color = BLANCO, r = 3, d = 3):
	pygame.draw.circle(pantalla, color, punto, r, d)


def Escala(punto, s):
	xp = p[0] * s[0]
	yp = p[1] * s[1]
	return [xp, yp]

