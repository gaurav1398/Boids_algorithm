import random
from boid import Boid

class RogueBoid(Boid):
    def update(self, dt, all_boids):
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]

        # Call the parent class update to apply the regular boid rules
        super().update(dt, all_boids)