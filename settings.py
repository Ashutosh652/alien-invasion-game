class Settings:
    """A class to store all settings for the game."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bgcolor = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
