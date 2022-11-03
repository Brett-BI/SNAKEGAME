import sys
import pygame

pygame.init()
size = width, height = 300, 400

speed = [2, 2]

black = 0, 0, 0


screen = pygame.display.set_mode(size)


ball = pygame.image.load("intro_ball.gif")

ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
'''
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
'''

class SnakeGame:
    def __init__(self): 
        self.status = 'chillin'




if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SnakeGame()
    ai.run_game()


