import pygame, random, sys

pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 1 - 호ㅏ면기본")


TARGET_KEYS = ['D', 'F', 'J', 'K']
LANES = [50, 150, 250, 350]
KEY_TO_LANE = {'D':50,'F':150,'J':250,'K':350}


clock = pygame.time.Clock()

class Note:
    def __init__(self, key):
        self.key = key
        self.x = KEY_TO_LANE[key]
        self.y = -100
        self.hit = False
    def update(self):
        self.y += 5
    def draw(self):
        pygame.draw.rect(screen,(255,255,255), (self.x-25,self.y,50,50))
        t = FONT.render(self.key,True,(0,0,0))
        screen.blit(t,(self.x-20,self.y))

notes = []
def spawn_note():
    k = random.choice(TARGET_KEYS)
    notes.append(Note(k))
spawn_note()




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



while True:
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 0, 0), (0, 500), (WIDTH, 500), 3)

    score_text = score_font.render(f"Score: {score} Miss: {miss}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # for note in notes:
    #     note.update()
    #     note.draw()
    #     if note.y > HEIGHT and not note.hit:
    #         miss += 1
    #         notes.remove(note)
    
    alive_notes = []
    for note in notes:
        note.update()
        note.draw()
        if note.y > HEIGHT and not note.hit:
            miss += 1
        else:
            alive_notes.append(note)
    notes = alive_notes


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            p = pygame.key.name(event.key).upper()
            for note in notes:
                if not note.hit and p==note.key and 450<note.y<540:
                    score += 1
                    note.hit = True
                    notes.remove(note)
                    break
                else:
                    pass
    

 

    if random.random() < 0.02:
        spawn_note()

    pygame.display.update()
    clock.tick(60)