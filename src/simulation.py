import astropy.constants;
import pygame;
import scipy;
import celestial_body;
from pygame import Vector2, Color;

class Simulation:
    G = astropy.constants.G.value;
    UNIVERSE_SCALE_FACTOR = 10000000000000000000000000;

    def __init__(self, screen, clock, running):
        self.screen = screen;
        self.clock = clock;
        self.running = running;

        self.bodies = [];

        #sun
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Sun",
            astropy.constants.M_sun.value / Simulation.UNIVERSE_SCALE_FACTOR * 10000,
            75,
            Vector2(1280/2, 720/2),
            Vector2(0, 0),
            Vector2(0, 0),
            Color(127, 127, 255)
        ));

        #earth
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Earth",
            astropy.constants.M_earth.value / Simulation.UNIVERSE_SCALE_FACTOR,
            15,
            Vector2(200, 100),
            Vector2(0.75, 0.75),
            Vector2(0, 0),
            Color(127, 127, 127)
        ));
        pass;

    def tick(self):
        for body in self.bodies:
            body.tick(self.bodies);
            print(body.name, body.acceleration);

        return;

    def render(self):
        for body in self.bodies:
            body.render(self.screen);

        return;

    def dispose(self):
        pass;
