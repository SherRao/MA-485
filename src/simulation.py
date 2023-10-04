import pygame;
import scipy;
import celestial_body;

class Simulation:
    G = scipy.constants.gravitational_constant;

    def __init__(self, screen, clock, running):
        self.screen = screen;
        self.clock = clock;
        self.running = running;

        self.bodies = [];
        self.bodies.append(celestial_body.CelestialBody(
            self,
            1,
            100,
            pygame.Vector2(500, 200),
            pygame.Vector2(1, 0),
            pygame.Vector2(-0.00021, 0),
            pygame.Color(127, 127, 255)
        ));

        self.bodies.append(celestial_body.CelestialBody(
            self,
            10,
            20,
            pygame.Vector2(200, 100),
            pygame.Vector2(-1, 0),
            pygame.Vector2(0.0001, 0),
            pygame.Color(127, 127, 127)
        ));
        pass;

    def tick(self):
        for body in self.bodies:
            body.tick(self.bodies);

        return;

    def render(self):
        for body in self.bodies:
            body.render(self.screen);

        return;

    def dispose(self):
        pass;
