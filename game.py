import pygame
import random
from screen_manager import show_opening_screen, game_over_screen, show_info_screen
from question_manager import generate_question, generate_answers
from particle_manager import add_particles, update_particles

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Game:
    def __init__(self, screen, width, height, assets):
        self.screen = screen
        self.width = width
        self.height = height
        self.assets = assets
        self.header_height = 70
        self.score = 0
        self.level = 1
        self.shield = False
        self.speed = 15
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.question, self.correct_answer = generate_question(self.level)
        self.answers = generate_answers(self.correct_answer)
        self.answer_positions = [[random.randint(50, self.width - 50), random.randint(self.header_height + 10, self.height - 50)] for _ in self.answers]

    def show_opening_screen(self):
        show_opening_screen(self.screen)

    def handle_movement(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        elif self.direction == 'DOWN':
            self.snake_pos[1] += 10
        elif self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif self.direction == 'RIGHT':
            self.snake_pos[0] += 10

        if self.snake_pos[0] >= self.width:
            self.snake_pos[0] = 0
        elif self.snake_pos[0] < 0:
            self.snake_pos[0] = self.width
        if self.snake_pos[1] >= self.height:
            self.snake_pos[1] = self.header_height
        elif self.snake_pos[1] < self.header_height:
            self.snake_pos[1] = self.height - 10

        self.snake_body.insert(0, list(self.snake_pos))
        self.snake_body.pop()

    def run_game_loop(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.assets['background_image'], (0, 0))
            self.handle_events()
            self.handle_movement()

            score_text = f"Score: {self.score}"
            level_text = f"Level: {self.level}"
            question_text = self.question

            score_render = self.assets['hud_font'].render(score_text, True, WHITE)
            level_render = self.assets['hud_font'].render(level_text, True, WHITE)
            question_render = self.assets['question_font'].render(question_text, True, BLACK)
            self.screen.blit(score_render, (45, 20))
            question_rect = question_render.get_rect(center=(self.width // 2, 35))
            self.screen.blit(question_render, question_rect)
            level_rect = level_render.get_rect(topright=(self.width - 45, 20))
            self.screen.blit(level_render, level_rect)
            
            self.screen.blit(self.assets['head_image'], self.snake_body[0])
            
            for pos in self.snake_body[1:-1]:  # Tubuh (tidak termasuk kepala dan ekor)
                self.screen.blit(self.assets['body_image'], pos)

            if len(self.snake_body) > 1:
                self.screen.blit(self.assets['tail_image'], self.snake_body[-1])

            for answer, pos in zip(self.answers, self.answer_positions):
                pygame.draw.circle(self.screen, BLUE, pos, 9)
                answer_render = self.assets['font'].render(str(answer), True, WHITE)
                answer_rect = answer_render.get_rect(center=pos)
                self.screen.blit(answer_render, answer_rect)

                if abs(self.snake_pos[0] - pos[0]) < 15 and abs(self.snake_pos[1] - pos[1]) < 15:
                    if answer == self.correct_answer:
                        self.score += 10
                        add_particles(self.snake_pos[0], self.snake_pos[1], GREEN)
                        if self.score % 50 == 0:
                            self.level += 1
                            self.answers.append(random.randint(0, 20))
                        self.snake_body.insert(-1, list(self.snake_body[-1]))
                        self.question, self.correct_answer = generate_question(self.level)
                        self.answers = generate_answers(self.correct_answer, len(self.answers))
                        self.answer_positions = [[random.randint(50, self.width - 50), random.randint(self.header_height + 10, self.height - 50)] for _ in self.answers]
                    else:
                        game_over_screen(self.screen)
                        running = False
                        break

            update_particles(self.screen)
            pygame.display.flip()
            clock.tick(self.speed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    self.change_to = 'RIGHT'
