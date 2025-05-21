
import pygame
import random
import sys

def iniciar_juego():
    pygame.init()

   
    WIDTH, HEIGHT = 500, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Esquiva o muere")

    
    BLUE = (0, 100, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    
    player_size = 50
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size - 10
    player_speed = 10

   
    enemy_size = 50
    enemy_speed = 5
    enemy_count = 5
    enemies = []
    for _ in range(enemy_count):
        x = random.randint(0, WIDTH - enemy_size)
        y = random.randint(-600, -50)
        enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

    
    font = pygame.font.SysFont(None, 36)
    score = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        
        for enemy in enemies:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                enemy.y = random.randint(-100, -40)
                enemy.x = random.randint(0, WIDTH - enemy_size)
                score += 1

            if player_rect.colliderect(enemy):
                print("Has muerto. Reiniciando juego.")
                pygame.time.delay(1000)
                iniciar_juego()  

            pygame.draw.rect(screen, RED, enemy)

        
        pygame.draw.rect(screen, BLUE, player_rect)

        
        score_text = font.render(f"Puntuació: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)


iniciar_juego()
