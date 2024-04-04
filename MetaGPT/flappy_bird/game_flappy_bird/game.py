import pygame
import random

class Bird:
    def __init__(self, x, y, width, height, velocity, acceleration, gravity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.acceleration = acceleration
        self.gravity = gravity

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))

class Pipe:
    def __init__(self, x, y, width, height, gap):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = gap
        self.score_counted = False

    def update(self):
        self.x -= 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y + self.gap + self.height, self.width, self.height))

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.bird = Bird(100, self.screen.get_height() / 2, 50, 50, 0, 0.5, 0.5)
        
        gap_height = 150  # Set this to the size you want for your gap
        pipe_height = 200  # Set this to the pipe height
        
        min_height = 50
        max_height = self.screen.get_height() - gap_height - pipe_height - min_height
        pipe_top_y = random.randint(min_height, max_height)
        
        self.pipes = [Pipe(600, pipe_top_y - pipe_height, 50, pipe_height, gap_height)]

        self.score = 0
        self.running = True

    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()

        if self.bird.y < 0 or self.bird.y + self.bird.height > self.screen.get_height():
            print("Bird is out of bounds")
            self.running = False

        for pipe in self.pipes:
            # Check horizontal overlap
            if self.bird.x < pipe.x + pipe.width and self.bird.x + self.bird.width > pipe.x:
                # Top pipe collision
                if self.bird.y < pipe.y + pipe.height:
                    print("Collision with top pipe")
                    self.running = False
                    break

                # Bottom pipe collision
                bottom_pipe_top = pipe.y + pipe.gap + pipe.height
                if self.bird.y + self.bird.height > bottom_pipe_top:
                    print("Collision with bottom pipe")
                    self.running = False
                    break
            
            if pipe.x + pipe.width < self.bird.x and not pipe.score_counted:
                self.score += 1
                pipe.score_counted = True

        if self.pipes[0].x < -50:
            self.pipes.pop(0)
            min_height = 50  # The minimum Y position at which the TOP of bottom pipe can start.
            gap_height = 150  # The vertical gap size between pipes.
            pipe_height = 200  # The height of each pipe.

            # This calculation ensures that the bottom pipe and top pipe will be fully visible on the screen.
            max_height = self.screen.get_height() - gap_height - pipe_height - min_height

            pipe_top_y = random.randint(min_height, max_height)
            self.pipes.append(Pipe(600, pipe_top_y - pipe_height, 50, pipe_height, gap_height))



    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)

        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()  # Update the full display Surface to the screen


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event triggered")
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.velocity = -10

    def run(self):
        while self.running:
            self.handle_input()
            self.draw()
            self.update()
            self.clock.tick(60)
