from abstract_character import AbstractCharacter


class HitPoints:
    def __init__(self, character: AbstractCharacter):
        self.character = character
        self.max_hit_points = 0
        self.current_hit_points = self.max_hit_points

    @property
    def current_hit_points(self):
        """Get current hit points."""
        return self.current_hit_points

    @current_hit_points.setter
    def current_hit_points(self, value):
        """Set current hit points."""
        if value <= self.max_hit_points:
            self.current_hit_points = value
        else:
            raise ValueError("Hit points cannot be greater than {}".format(self.max_hit_points))
