import pygame
import random
import sys

pygame.init()

# Tamaño de la ventana
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evita los enemigos")

# Colores
BLUE = (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Jugador
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Enemigos
enemy_size = 50
enemy_speed = 5
enemy_count = 5  # Número de enemigos al mismo tiempo
enemies = []

for _ in range(enemy_count):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(-600, -50)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

# Fuente para el contador
font = pygame.font.SysFont(None, 36)
score = 0

# Reloj
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Mover enemigos
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = random.randint(-100, -40)
            enemy.x = random.randint(0, WIDTH - enemy_size)
            score += 1  # Suma puntos por esquivar

        if player_rect.colliderect(enemy):
            print("💥 GAME OVER 💥")
            running = False

        pygame.draw.rect(screen, RED, enemy)

    # Dibujar jugador
    pygame.draw.rect(screen, BLUE, player_rect)

    # Mostrar puntuación
    score_text = font.render(f"Puntuació: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
