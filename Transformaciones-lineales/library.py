import pygame
import math

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

def rotacionHoraria(p, angulo):
    ar = math.radians(angulo)
    xp = (p[0] * math.cos(ar)) + (p[1] * math.sin(ar))
    yp = -(p[0] * math.sin(ar)) + (p[1] * math.cos(ar))
    return [int (xp), int (yp)]

def rotacionAntihoraria(p, angulo):
    ar=math.radians(angulo)
    xp = (p[0] * math.cos(ar)) - (p[1] * math.sin(ar))
    yp = (p[0] * math.sin(ar)) + (p[1] * math.cos(ar))
    return [int (xp), int (yp)]


def traslacion(p, d):
    xd = p[0] + d[0]
    yd = p[1] + d[1]
    return [xd, yd]

# Pto fijo, p= punto a escalar; escal= a lo que se desea escalar
def escalapf(ptoFijo, p, escal):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=[((p1[0])*escal), ((p1[1])*escal)]
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

# Pto fijo, p= punto a rotar; o = origen; r= angulo que se desea rotar
def rotacionpfah(ptoFijo, p, o, r):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=rotacionHoraria(p1, r)
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

# Pto fijo, p= punto a rotar;0 = origen; r= angulo al que se desea rotar
def rotacionpfh(ptoFijo, p, o, r):
    p1=[(-ptoFijo[0]+p[0]), (-ptoFijo[1]+p[1])]
    p1es=rotacionAntihoraria(p1, r)
    p1e=[(ptoFijo[0]+p1es[0]), (ptoFijo[1]+p1es[1])]
    return p1e

# r: radio
def polar_a_cartesiano(r, angulo):
    ar = math.radians(angulo)
    x = r * math.cos(ar)
    y = r * math.sin(ar)
    return [int(x), int(y)]