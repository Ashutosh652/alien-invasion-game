class Settings:
    """A class to store all settings for the game."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bgcolor = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        # Ship Settings
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Alien Settings
        self.fleet_direction = 1  # fleet_direction of 1 represents right direction and -1 represents left direction.

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
