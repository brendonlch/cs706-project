import pygame
from pygame.locals import *

class Game:
    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height
        self.ball_speed = 5
        self.paddle_speed = 7
        self.score = 0
        self.ai_speed = 5
        self.player_paddle = Paddle(0, height // 2, 10, 60, self.paddle_speed)
        self.ai_paddle = Paddle(width - 10, height // 2, 10, 60, self.ai_speed)
        self.ball = Ball(width // 2, height // 2, 8, self.ball_speed, self.ball_speed)

    def update(self):
        self.player_paddle.update()
        self.ai_paddle.update()
        self.ball.update()

    def draw(self, screen: pygame.Surface):
        self.player_paddle.draw(screen)
        self.ai_paddle.draw(screen)
        self.ball.draw(screen)

    def check_collision(self):
        if self.ball.rect.colliderect(self.player_paddle.rect) or self.ball.rect.colliderect(self.ai_paddle.rect):
            self.ball.speed_x = -self.ball.speed_x  

    def increase_speed(self):
        self.ball_speed += 1
        self.paddle_speed += 1
        self.ai_speed += 1

    def reset(self):
        self.score = 0
        self.ball_speed = 5
        self.paddle_speed = 7
        self.ai_speed = 5
        self.player_paddle = Paddle(0, self.screen_height // 2, 10, 60, self.paddle_speed)
        self.ai_paddle = Paddle(self.screen_width - 10, self.screen_height // 2, 10, 60, self.ai_speed)
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2, 8, self.ball_speed, self.ball_speed)

# Define the Paddle class
class Paddle:
    def __init__(self, x: int, y: int, width: int, height: int, speed: int):
        self.rect = pygame.Rect(x, y, width, height) # Use pygame.Rect for easy rect calculations
        self.speed = speed
        self.dy = 0  # Change in y for paddle movement

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dy = -self.speed
        elif keys[pygame.K_DOWN]:
            self.dy = self.speed
        else:
            self.dy = 0

        # Update the paddle's position
        self.rect.y += self.dy

        # Prevent the paddle from moving off the screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

# Define the Ball class
class Ball:
    def __init__(self, x: int, y: int, radius: int, speed_x: int, speed_y: int):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2) # Ball's rect for collision
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()

    def update(self):
        # Update the ball's position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the top and bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y = -self.speed_y
        
        # Bounce off the left and right of the screen (to be changed to score a point)
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x = -self.speed_x

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.radius)