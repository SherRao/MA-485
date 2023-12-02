import astropy.constants;
import pygame;
import scipy;
import celestial_body;
from pygame import Vector2, Color;

class Simulation:
    G = astropy.constants.G.value;
    AU = 1.496e8 * 1000
    DAYS_PER_SECOND = 1;
    UNIVERSE_TIMESTEP = (60 * 60 * 24) * DAYS_PER_SECOND;
    UNIVERSE_SCALE_FACTOR = 250 / AU;
    WIDTH, HEIGHT = (1920, 1080);

    def __init__(self, screen, clock, running):
        self.screen = screen;
        self.clock = clock;
        self.running = running;
        self.bodies = [];
        self.font = pygame.font.SysFont("Consolas", 18);
        self.debug = True;

        # sun
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Sun",
            astropy.constants.M_sun.value,
            20, #astropy.constants.R_sun.value * self.UNIVERSE_SCALE_FACTOR,
            Vector2(0, 0),
            Vector2(0, 0),
            Color(253, 184, 19)
        ));

        # earth
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Earth",
            astropy.constants.M_earth.value,
            10, # astropy.constants.R_earth.value * self.UNIVERSE_SCALE_FACTOR,
            Vector2(1.496e11, 0),
            Vector2(0, 29.783e3),
            Color(40, 122, 184)
        ));

        # mars
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Mars",
            6.39e23, #astropy.constants.M_mars.value,
            10, # astropy.constants.R_mars.value * self.UNIVERSE_SCALE_FACTOR,
            Vector2(2.279e11, 0),
            Vector2(0, 24.077e3),
            Color(184, 40, 40)
        ));

        # jupiter
        self.bodies.append(celestial_body.CelestialBody(
            self,
            "Jupiter",
            astropy.constants.M_jup.value,
            12, # astropy.constants.R_jup.value * self.UNIVERSE_SCALE_FACTOR,
            Vector2(7.785e11, 0),
            Vector2(0, 13.07e3),
            Color(156, 63, 48)
        ));

        return;

    def tick(self):
        for body in self.bodies:
            body.tick();

        return;

    def render(self):
        for body in self.bodies:
            body.render(self.screen);

        if(self.debug):
            self.render_debug_data();

        return;

    def scale(self, factor):
        self.UNIVERSE_SCALE_FACTOR += factor/self.AU;
        return;


    def render_debug_data(self):
        def f(num):
            return num * self.UNIVERSE_SCALE_FACTOR;

        earth = self.bodies[1];
        jupiter = self.bodies[2];
        sun = self.bodies[0];

        text = self.font.render(f"FPS: {str(int(self.clock.get_fps()))}", True, (255, 255, 255));
        self.screen.blit(text, (10, 10));

        text = self.font.render(f"Mouse: {str(pygame.mouse.get_pos())}", True, (255, 255, 255));
        self.screen.blit(text, (10, 30));

        text = self.font.render(f"Earth: P={f(earth.position)}, M={f(earth.mass)}, R={f(earth.radius)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 70));

        text = self.font.render(f"Earth Raw: P={earth.position}, M={earth.mass}, R={earth.radius}", True, (255, 255, 255));
        self.screen.blit(text, (10, 90));

        text = self.font.render(f"Jupiter: P={f(jupiter.position)}, M={f(jupiter.mass)}, R={f(jupiter.radius)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 110));

        text = self.font.render(f"Jupiter Raw: P={jupiter.position}, M={jupiter.mass}, R={jupiter.radius}", True, (255, 255, 255));
        self.screen.blit(text, (10, 130));

        text = self.font.render(f"Sun: P={f(sun.position)}, M={f(sun.mass)}, R={f(sun.radius)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 150));

        text = self.font.render(f"Sun Raw: P={sun.position}, M={sun.mass}, R={sun.radius}", True, (255, 255, 255));
        self.screen.blit(text, (10, 170));

        text = self.font.render(f"Scale: {str(self.UNIVERSE_SCALE_FACTOR)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 190));

        text = self.font.render(f"G: {str(self.G)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 210));
        return;

    def screen_to_real_coords(self, pos: Vector2):
        cx, cy = self.WIDTH // 2, self.HEIGHT // 2;
        return Vector2(
            (pos.x - cx) / self.UNIVERSE_SCALE_FACTOR,
            (pos.y - cy) / -self.UNIVERSE_SCALE_FACTOR
        );

    def real_to_screen_coords(self, pos: Vector2):
        cx, cy = self.WIDTH // 2, self.HEIGHT // 2;
        return Vector2(
            cx + pos.x * self.UNIVERSE_SCALE_FACTOR,
            cy + pos.y * -self.UNIVERSE_SCALE_FACTOR
        );


    def dispose(self):
        return;


