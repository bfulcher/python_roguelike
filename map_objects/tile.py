class Tile:
    # A tile on a map. It may or may not be blocked, and may or may not block sight.
    def __init__(self, blocked, blocked_sight=None):
        self.blocked = blocked

        # By default, if a tile is blocked, it also blocks sight
        if blocked_sight is None:
            blocked_sight = blocked

        self.blocked_sight = blocked_sight

        self.explored = False