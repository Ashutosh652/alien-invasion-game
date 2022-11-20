import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, ai_game) -> None:
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.instructions_font = pygame.font.SysFont(None, 18)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bgcolor
        )

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = "High Score: {:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bgcolor
        )

        # Display the high score at the top center of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw scores, level and remaining ships(lives) to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bgcolor
        )

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how may ships(lives) are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_instructions(self):
        """Turn the instructions into rendered images."""
        ins1 = """Press [p] to play or stop the game."""
        ins2 = "Press [Space] to shoot."
        ins3 = "Press [q] to quit."
        self.ins1_image = self.instructions_font.render(
            ins1, True, self.text_color, self.settings.bgcolor
        )
        self.ins2_image = self.instructions_font.render(
            ins2, True, self.text_color, self.settings.bgcolor
        )
        self.ins3_image = self.instructions_font.render(
            ins3, True, self.text_color, self.settings.bgcolor
        )

        # Position the instructions on the bottom left on top of one another.
        self.ins3_rect = self.ins3_image.get_rect()
        self.ins2_rect = self.ins2_image.get_rect()
        self.ins1_rect = self.ins1_image.get_rect()
        self.ins3_rect.bottomleft = self.screen_rect.bottomleft
        self.ins2_rect.bottomleft = self.ins3_rect.topleft
        self.ins1_rect.bottomleft = self.ins2_rect.topleft

    def show_instructions(self):
        """Show the instructions on the screen."""
        self.screen.blit(self.ins3_image, self.ins3_rect)
        self.screen.blit(self.ins2_image, self.ins2_rect)
        self.screen.blit(self.ins1_image, self.ins1_rect)
