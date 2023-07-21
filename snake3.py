import pygame
import sys
import random

# Configuración de pantalla
ANCHO, ALTO = 800, 600
TAMANO_CELDA = 20
ANCHO_CELDAS = ANCHO // TAMANO_CELDA
ALTO_CELDAS = ALTO // TAMANO_CELDA

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

def dibujar_celda(pantalla, color, fila, columna):
    x = columna * TAMANO_CELDA
    y = fila * TAMANO_CELDA
    pygame.draw.rect(pantalla, color, (x, y, TAMANO_CELDA, TAMANO_CELDA))

def mostrar_mensaje(pantalla, mensaje):
    font = pygame.font.Font(None, 36)
    texto = font.render(mensaje, True, BLANCO)
    x = (ANCHO - texto.get_width()) // 2
    y = (ALTO - texto.get_height()) // 2
    pantalla.blit(texto, (x, y))
    pygame.display.flip()

def snake_juego():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Snake')
    reloj = pygame.time.Clock()

    snake = [(ANCHO_CELDAS // 2, ALTO_CELDAS // 2)]
    direccion = (0, -1)
    comida = (random.randint(0, ANCHO_CELDAS - 1), random.randint(0, ALTO_CELDAS - 1))
    crecer = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != (0, 1):
                    direccion = (0, -1)
                elif evento.key == pygame.K_DOWN and direccion != (0, -1):
                    direccion = (0, 1)
                elif evento.key == pygame.K_LEFT and direccion != (1, 0):
                    direccion = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direccion != (-1, 0):
                    direccion = (1, 0)

        nueva_cabeza = (snake[0][0] + direccion[0], snake[0][1] + direccion[1])
        snake.insert(0, nueva_cabeza)

        if nueva_cabeza == comida:
            comida = (random.randint(0, ANCHO_CELDAS - 1), random.randint(0, ALTO_CELDAS - 1))
            crecer = True

        if not crecer:
            snake.pop()
        else:
            crecer = False

        pantalla.fill(NEGRO)
        for celda in snake:
            dibujar_celda(pantalla, VERDE, celda[1], celda[0])
        dibujar_celda(pantalla, ROJO, comida[1], comida[0])

        if snake[0][0] < 0 or snake[0][0] >= ANCHO_CELDAS or snake[0][1] < 0 or snake[0][1] >= ALTO_CELDAS:
            mostrar_mensaje(pantalla, "¡Perdiste! Presiona 'R' para reiniciar.")
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            return
        pygame.display.flip()
        reloj.tick(10)

# ... (código anterior)

def mostrar_puntaje(pantalla, puntaje):
    font = pygame.font.Font(None, 30)
    texto = font.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

def snake_juego():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Snake')
    reloj = pygame.time.Clock()

    snake = [(ANCHO_CELDAS // 2, ALTO_CELDAS // 2)]
    direccion = (0, -1)
    comida = (random.randint(0, ANCHO_CELDAS - 1), random.randint(0, ALTO_CELDAS - 1))
    crecer = False
    puntaje = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != (0, 1):
                    direccion = (0, -1)
                elif evento.key == pygame.K_DOWN and direccion != (0, -1):
                    direccion = (0, 1)
                elif evento.key == pygame.K_LEFT and direccion != (1, 0):
                    direccion = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direccion != (-1, 0):
                    direccion = (1, 0)

        nueva_cabeza = (snake[0][0] + direccion[0], snake[0][1] + direccion[1])
        snake.insert(0, nueva_cabeza)

        if nueva_cabeza == comida:
            comida = (random.randint(0, ANCHO_CELDAS - 1), random.randint(0, ALTO_CELDAS - 1))
            crecer = True
            puntaje += 10

        if not crecer:
            snake.pop()
        else:
            crecer = False

        pantalla.fill(NEGRO)
        for celda in snake:
            dibujar_celda(pantalla, VERDE, celda[1], celda[0])
        dibujar_celda(pantalla, ROJO, comida[1], comida[0])

        mostrar_puntaje(pantalla, puntaje)  # Muestra el puntaje en la pantalla

        if snake[0][0] < 0 or snake[0][0] >= ANCHO_CELDAS or snake[0][1] < 0 or snake[0][1] >= ALTO_CELDAS:
            mostrar_mensaje(pantalla, f"¡Perdiste! Puntaje final: {puntaje}. Presiona 'R' para reiniciar.")
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            return
        pygame.display.flip()
        reloj.tick(10)

if __name__ == "__main__":
    snake_juego()
