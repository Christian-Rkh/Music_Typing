import pygame, random, sys

pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 1 - 호ㅏ면기본")


clock = pygame.time.Clock()




FONT = pygame.font.SysFont(None, 72)

score_font = pygame.font.SysFont(None, 36)
score = 0
miss = 0

TARGET_KEYS = ['D', 'F', 'J', 'K']
LANES = [50, 150, 250, 350]

KEY_TO_LANE = {
    'D': LANES[0],
    'F': LANES[1],
    "J": LANES[2],
    "K": LANES[3] 
}

key_y = -100
key_char = random.choice(TARGET_KEYS)
key_x = KEY_TO_LANE[key_char]
idx = random.randint(0, 3)
key_char = TARGET_KEYS[idx]
key_x = LANES[idx]
fall_speed = 5

def reset_key():
    global key_y, key_x, key_char
    key_y = -100

    i = random.randint(0, 3)
    key_char = TARGET_KEYS[i]
    key_x = LANES[i]

while True:
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 0, 0), (0, 500), (WIDTH, 500), 3)

    score_text = score_font.render(f"Score: {score} Miss: {miss}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    pygame.draw.rect(screen, (255, 255, 255), (key_x - 25, key_y, 50, 50))
    text = FONT.render(key_char, True, (0, 0, 0))
    screen.blit(text, (key_x - 20, key_y))

    key_y += fall_speed
    if key_y > HEIGHT:
        reset_key()
        miss += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if 420 < key_y < 540:
                if event.unicode.upper() == key_char:
                    score += 1
                    reset_key()

    pygame.display.update()
    clock.tick(60)