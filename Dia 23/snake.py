import pygame
import random

# https://github.com/lucmadev/30-Dias-de-Python

# pip install pygame 

pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
BLOCK = 20
FPS = 7

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(win, GREEN, (x, y, BLOCK, BLOCK))

def main():
    # Posición inicial (centro)
    x, y = WIDTH // 2, HEIGHT // 2

    # Inicializamos la serpiente con 3 bloques (evita colisión instantánea)
    snake = [(x, y), (x - BLOCK, y), (x - 2*BLOCK, y)]

    # Direccion inicial: moviéndose hacia la derecha
    dx, dy = BLOCK, 0

    # Crear la primera comida en una posición válida (alineada a la grilla)
    def random_food():
        return (random.randrange(0, WIDTH, BLOCK), random.randrange(0, HEIGHT, BLOCK))
    food = random_food()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # prevenir que el jugador haga 180° inmediato
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK, 0

        # Mover cabeza
        x += dx
        y += dy

        # Colisiones con paredes
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False
            break

        # Nueva cabeza
        new_head = (x, y)

        # Colisión con el cuerpo: chequear contra snake[:-1] porque la cola se va a mover
        if new_head in snake[:-1]:
            running = False
            break

        snake.append(new_head)

        # Comer comida
        if new_head == food:
            food = random_food()
            # asegurarnos que la comida no caiga sobre la serpiente
            while food in snake:
                food = random_food()
        else:
            snake.pop(0)  # mover: quitar cola

        # Dibujado
        win.fill(BLACK)
        pygame.draw.rect(win, RED, (*food, BLOCK, BLOCK))
        draw_snake(snake)
        pygame.display.update()

    # Fin del juego
    pygame.quit()

if __name__ == "__main__":
    main()
