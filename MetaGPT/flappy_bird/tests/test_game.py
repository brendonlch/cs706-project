import unittest
import pygame
import random
from game_flappy_bird.game import Bird, Pipe, Game

class TestBird(unittest.TestCase):

    def setUp(self):
        self.bird = Bird(100, 100, 50, 50, 0, 0.5, 0.5)

    def test_init(self):
        self.assertEqual(self.bird.x, 100)
        self.assertEqual(self.bird.y, 100)
        self.assertEqual(self.bird.width, 50)
        self.assertEqual(self.bird.height, 50)
        self.assertEqual(self.bird.velocity, 0)
        self.assertEqual(self.bird.acceleration, 0.5)
        self.assertEqual(self.bird.gravity, 0.5)

    def test_update(self):
        self.bird.update()
        self.assertEqual(self.bird.velocity, 0.5)
        self.assertEqual(self.bird.y, 100.5)

    def test_draw(self):
        screen = pygame.display.set_mode((600, 500))
        self.bird.draw(screen)
        pygame.display.update()
        self.assertEqual(screen.get_at((100, 100)), (255, 255, 0))

class TestPipe(unittest.TestCase):

    def setUp(self):
        self.pipe = Pipe(100, 100, 50, 200, 100)

    def test_init(self):
        self.assertEqual(self.pipe.x, 100)
        self.assertEqual(self.pipe.y, 100)
        self.assertEqual(self.pipe.width, 50)
        self.assertEqual(self.pipe.height, 200)
        self.assertEqual(self.pipe.gap, 100)

    def test_update(self):
        self.pipe.update()
        self.assertEqual(self.pipe.x, 95)

    def test_draw(self):
        screen = pygame.display.set_mode((600, 500))
        self.pipe.draw(screen)
        pygame.display.update()
        self.assertEqual(screen.get_at((100, 100)), (0, 255, 0))
        self.assertEqual(screen.get_at((100, 300)), (0, 255, 0))

class TestGame(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((600, 500))
        self.clock = pygame.time.Clock()
        self.game = Game(self.screen, self.clock)

    def test_init(self):
        self.assertEqual(self.game.screen, self.screen)
        self.assertEqual(self.game.clock, self.clock)
        self.assertEqual(self.game.bird.x, 100)
        self.assertEqual(self.game.bird.y, 100)
        self.assertEqual(self.game.pipes[0].x, 600)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.running, True)

    def test_update(self):
        self.game.update()
        self.assertEqual(self.game.bird.velocity, 0.5)
        self.assertEqual(self.game.bird.y, 100.5)
        self.assertEqual(self.game.pipes[0].x, 595)

    def test_draw(self):
        self.game.draw()
        pygame.display.update()
        self.assertEqual(self.screen.get_at((100, 100)), (255, 255, 0))
        self.assertEqual(self.screen.get_at((600, 100)), (0, 255, 0))

    def test_handle_input(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        self.game.handle_input()
        self.assertEqual(self.game.running, False)

    def test_run(self):
        self.game.run()
        self.assertEqual(self.game.running, False)

if __name__ == '__main__':
    unittest.main()
