import pygame
import random
import numpy as np

# --- Parametry gry ---
BOARD_SIZE = 10
CELL_SIZE = 50
SCREEN_SIZE = BOARD_SIZE * CELL_SIZE

HIDE_SPOTS = [(1,1), (3,7), (6,2), (8,8)]

ACTIONS = ['up', 'down', 'left', 'right', 'hide', 'unhide']

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Berka AI - Q-Learning")

font = pygame.font.SysFont(None, 24)

def move_pos(pos, action):
    x,y = pos
    if action == 'up' and y > 0:
        y -= 1
    elif action == 'down' and y < BOARD_SIZE -1:
        y += 1
    elif action == 'left' and x > 0:
        x -= 1
    elif action == 'right' and x < BOARD_SIZE -1:
        x += 1
    return (x,y)

class Agent:
    def __init__(self, name):
        self.name = name
        self.pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        self.is_hiding = False
        self.q_table = {}
    
    def get_state(self, seeker_pos, hider_pos, hider_hide):
        return (seeker_pos, hider_pos, hider_hide)

    def choose_action(self, state, epsilon=0.1):
        if random.random() < epsilon:
            return random.choice(ACTIONS)
        qs = [self.q_table.get((state, a), 0) for a in ACTIONS]
        max_q = max(qs)
        max_actions = [a for a,q in zip(ACTIONS, qs) if q == max_q]
        return random.choice(max_actions)

    def update_q(self, state, action, reward, next_state, alpha=0.5, gamma=0.9):
        old_q = self.q_table.get((state, action), 0)
        next_max = max([self.q_table.get((next_state, a), 0) for a in ACTIONS])
        new_q = old_q + alpha * (reward + gamma * next_max - old_q)
        self.q_table[(state, action)] = new_q

def draw_board(seeker, hider):
    screen.fill((50, 150, 50))  # zielone tło planszy
    
    # rysuj kratki
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (100, 200, 100), rect, 1)
    
    # rysuj kryjówki
    for spot in HIDE_SPOTS:
        rect = pygame.Rect(spot[0]*CELL_SIZE, spot[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0, 0, 139), rect)  # ciemny niebieski
    
    # rysuj szukającego
    seeker_rect = pygame.Rect(seeker.pos[0]*CELL_SIZE+5, seeker.pos[1]*CELL_SIZE+5, CELL_SIZE-10, CELL_SIZE-10)
    pygame.draw.ellipse(screen, (255, 0, 0), seeker_rect)  # czerwony
    
    # rysuj ukrywającego
    color = (0, 255, 0) if not hider.is_hiding else (0, 100, 0)  # jasny lub ciemny zielony
    hider_rect = pygame.Rect(hider.pos[0]*CELL_SIZE+10, hider.pos[1]*CELL_SIZE+10, CELL_SIZE-20, CELL_SIZE-20)
    pygame.draw.ellipse(screen, color, hider_rect)
    
    # tekst status
    text = font.render(f"Ukrywający {'ukryty' if hider.is_hiding else 'widoczny'}", True, (255,255,255))
    screen.blit(text, (5, SCREEN_SIZE - 30))

def play_episode(seeker, hider, training=True, epsilon=0.1, max_steps=100):
    seeker.pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    hider.pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    hider.is_hiding = False
    
    for step in range(max_steps):
        state = seeker.get_state(seeker.pos, hider.pos, hider.is_hiding)
        seeker_action = seeker.choose_action(state, epsilon)
        hider_action = hider.choose_action(state, epsilon)

        # ruch szukającego
        if seeker_action in ['up','down','left','right']:
            seeker.pos = move_pos(seeker.pos, seeker_action)
        # ruch ukrywającego lub kryjówka
        if hider_action in ['up','down','left','right']:
            if hider.is_hiding:
                hider.is_hiding = False
            hider.pos = move_pos(hider.pos, hider_action)
        elif hider_action == 'hide':
            if hider.pos in HIDE_SPOTS:
                hider.is_hiding = True
        elif hider_action == 'unhide':
            hider.is_hiding = False

        # nagrody
        reward_seeker = -0.01
        reward_hider = 0.01
        
        caught = (seeker.pos == hider.pos and not hider.is_hiding)
        if caught:
            reward_seeker += 1
            reward_hider -= 1
            if training:
                next_state = seeker.get_state(seeker.pos, hider.pos, hider.is_hiding)
                seeker.update_q(state, seeker_action, reward_seeker, next_state)
                hider.update_q(state, hider_action, reward_hider, next_state)
            return True
        
        if hider.is_hiding:
            reward_hider += 0.05
        
        next_state = seeker.get_state(seeker.pos, hider.pos, hider.is_hiding)
        if training:
            seeker.update_q(state, seeker_action, reward_seeker, next_state)
            hider.update_q(state, hider_action, reward_hider, next_state)

    return False

def train(seeker, hider, episodes=1000):
    caught_count = 0
    for ep in range(episodes):
        caught = play_episode(seeker, hider, training=True, epsilon=0.2)
        if caught:
            caught_count += 1
        if ep % 100 == 0:
            print(f"Epizod {ep}, złapanych: {caught_count}")
    print("Trening zakończony")
    return caught_count

def demo(seeker, hider):
    clock = pygame.time.Clock()
    running = True

    max_steps_per_round = 50
    step = 0
    caught = False

    def reset_positions():
        seeker.pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        hider.pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        hider.is_hiding = False

    reset_positions()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not caught and step < max_steps_per_round:
            state = seeker.get_state(seeker.pos, hider.pos, hider.is_hiding)

            # Szukający robi 2 ruchy na 1 iterację:
            for _ in range(2):
                seeker_action = seeker.choose_action(state, epsilon=0)
                if seeker_action in ['up','down','left','right']:
                    seeker.pos = move_pos(seeker.pos, seeker_action)
                # update stan, żeby drugi ruch brał pod uwagę nową pozycję
                state = seeker.get_state(seeker.pos, hider.pos, hider.is_hiding)

            # Ukrywający robi 1 ruch
            hider_action = hider.choose_action(state, epsilon=0)
            if hider_action in ['up','down','left','right']:
                if hider.is_hiding:
                    hider.is_hiding = False
                hider.pos = move_pos(hider.pos, hider_action)
            elif hider_action == 'hide':
                if hider.pos in HIDE_SPOTS:
                    hider.is_hiding = True
            elif hider_action == 'unhide':
                hider.is_hiding = False

            caught = (seeker.pos == hider.pos and not hider.is_hiding)
            step += 1

        if caught or step >= max_steps_per_round:
            reset_positions()
            step = 0
            caught = False

        draw_board(seeker, hider)
        pygame.display.flip()
        clock.tick(10)  # zwiększamy fps dla płynności

    pygame.quit()

if __name__ == "__main__":
    seeker = Agent("Berek")
    hider = Agent("Ukrywający")
    train(seeker, hider, episodes=2000)
    demo(seeker, hider)
