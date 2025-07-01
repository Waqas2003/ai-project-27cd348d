import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        self.size = 800
        self.snake_size = 20
        self.snake_speed = 10
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.food_pos = [random.randrange(1, self.size // self.snake_size) * self.snake_size, 
                         random.randrange(1, self.size // self.snake_size) * self.snake_size]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

    def run(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.run_game()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.change_to = 'RIGHT'

            self.validate_direction()
            self.update_snake()
            self.check_collision()
            self.display_game()
            self.clock.tick(self.snake_speed)

    def validate_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update_snake(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= self.snake_size
        if self.direction == 'DOWN':
            self.snake_pos[1] += self.snake_size
        if self.direction == 'LEFT':
            self.snake_pos[0] -= self.snake_size
        if self.direction == 'RIGHT':
            self.snake_pos[0] += self.snake_size
        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos == self.food_pos:
            self.score += 1
            self.food_pos = [random.randrange(1, self.size // self.snake_size) * self.snake_size, 
                             random.randrange(1, self.size // self.snake_size) * self.snake_size]
        else:
            self.snake_body.pop()

    def check_collision(self):
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.size - self.snake_size:
            self.game_over()
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.size - self.snake_size:
            self.game_over()
        for block in self.snake_body[1:]:
            if self.snake_pos == block:
                self.game_over()

    def display_game(self):
        self.game_window.fill((255, 255, 255))
        for pos in self.snake_body:
            pygame.draw.rect(self.game_window, (0, 255, 0), pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size))
        pygame.draw.rect(self.game_window, (255, 0, 0), pygame.Rect(self.food_pos[0], self.food_pos[1], self.snake_size, self.snake_size))
        pygame.display.flip()

    def game_over(self):
        pygame.quit()
        sys.exit()