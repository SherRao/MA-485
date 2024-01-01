from webbrowser import get
import astropy.constants;
import pygame;
import scipy;

from celestial_body import CelestialBody;
from pygame import Vector3, Color;
from constants import *;

class Simulation:
    """
    The simulation class is responsible for managing the simulation state
    by updating the logic and physics of every celestial body, as well as
    rendering the simulation to the screen.
    """
    G = astropy.constants.G.value;
    AU = 1.496e8 * 1000
    DAYS_PER_SECOND = 0.25;
    UNIVERSE_TIMESTEP = (60 * 60 * 24) * DAYS_PER_SECOND;
    UNIVERSE_SCALE_FACTOR = 250 / AU;
    UNIVERSE_BODY_SCALE_FACTOR = UNIVERSE_SCALE_FACTOR * 500000000;

    WIDTH, HEIGHT = (1366, 768);
    CENTER_X, CENTER_Y, CENTER_Z = (WIDTH // 2, HEIGHT // 2, 0);
    MAX_ORBITAL_PATH_LENGTH = 10000;

    def __init__(self, screen, clock):
        """
        Initializes the simulation with the given screen and clock.

        @param screen: The pygame screen to render to.
        @param clock: The pygame clock to use for timing.
        """
        self.screen = screen;
        self.clock = clock;
        self.running = True;
        self.bodies = [];
        self.font = pygame.font.SysFont("Consolas", 18);
        self.debug = True;
        self.ticks = 0;

        self.selected_body = None;
        self.bodies.append(self.get_sun());
        self.bodies.append(self.get_mercury());
        self.bodies.append(self.get_venus());
        self.bodies.append(self.get_earth());
        self.bodies.append(self.get_mars());
        self.bodies.append(self.get_jupiter());
        self.bodies.append(self.get_saturn());
        self.bodies.append(self.get_uranus());
        self.bodies.append(self.get_neptune());
        self.bodies.append(self.get_pluto());
        return;


    def tick(self):
        """
        Updates the simulation state by one tick.
        """
        self.check_events();
        for body in self.bodies:
            body.tick();

        self.ticks += 1;
        return;


    def render(self):
        """
        Renders the simulation to the screen.
        """
        for body in self.bodies:
            body.render(self.screen);

        if(self.debug):
            self.render_debug_data();

        points = [(10, 10), (11, 11), (12, 12), (50, 50), (100, 100)];
        pygame.draw.lines(self.screen, Color(255, 0, 0), False, points, 1);
        return;


    def check_events(self):
        """
        Checks for pygame events and handles them accordingly.
        """
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False;

            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.check_for_planet_selection();

        return;


    def check_keys(self):
        """
        Checks for pygame key presses and handles them accordingly.
        """
        keys_pressed = pygame.key.get_pressed();
        if(keys_pressed[pygame.K_ESCAPE]):
            self.running = False;
            print("Debug: ", self.debug);

        if(keys_pressed[pygame.K_p]):
            self.debug = not self.debug;

        if(keys_pressed[pygame.K_q]):
            self.scale(1);
            print("Scale: ", self.UNIVERSE_SCALE_FACTOR);

        if(keys_pressed[pygame.K_w]):
            self.scale(-1);
            print("Scale: ", self.UNIVERSE_SCALE_FACTOR);

        if(keys_pressed[pygame.K_e]):
            self.timestep(1);
            print("Timestep: ", self.UNIVERSE_TIMESTEP);

        if(keys_pressed[pygame.K_r]):
            self.timestep(-1);
            print("Timestep: ", self.UNIVERSE_TIMESTEP);

        if(keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]):
            self.pan_camera(dy=5);
            print("Panned: ", (self.CENTER_X, self.CENTER_Y));

        if(keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]):
            self.pan_camera(dy=-5);
            print("Panned: ", (self.CENTER_X, self.CENTER_Y));

        if(keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]):
            self.pan_camera(dx=5);
            print("Panned: ", (self.CENTER_X, self.CENTER_Y));

        if(keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]):
            self.pan_camera(dx=-5);
            print("Panned: ", (self.CENTER_X, self.CENTER_Y));

        return;


    def check_for_planet_selection(self):
        """
        Checks if the mouse is hovering and clicking over a planet and
        selects it if so.
        """
        mouse_pos = pygame.mouse.get_pos();
        for body in self.bodies:
            if(body.contains_point(mouse_pos)):
                print("Selected: ", body.name);
                self.selected_body = body;
                break;

        return;


    def scale(self, factor):
        """
        Scales distances and sizes in the universe by the given factor.

        @example:
            scale(2) -> 2x
            scale(0.5) -> 1/2x

        @param factor: The factor to scale by.
        """
        future_scale = self.UNIVERSE_SCALE_FACTOR + (factor / self.AU);
        if(future_scale > 0):
            self.UNIVERSE_SCALE_FACTOR = future_scale;
        return;


    def pan_camera(self, dx=0, dy=0, dz=0):
        """
        Pans the camera by the given amount. Each parameter is optional
        and defaults to 0.

        @param dx: The amount to pan the camera in the x direction.
        @param dy: The amount to pan the camera in the y direction.
        @param dz: The amount to pan the camera in the z direction.
        """
        self.CENTER_X += dx;
        self.CENTER_Y += dy;
        self.CENTER_Z += dz;
        return;


    def timestep(self, factor):
        """
        Changes the timestep of the simulation by the given factor.

        @example:
            timestep(2) -> 2x
            timestep(0.5) -> 1/2x

        @param factor: The factor to change the timestep by.
        """
        self.DAYS_PER_SECOND = max(1/86400, self.DAYS_PER_SECOND - (.05 * factor));
        self.UNIVERSE_TIMESTEP = (60 * 60 * 24) * self.DAYS_PER_SECOND;
        return;


    def screen_to_real_coords(self, pos: Vector3):
        """
        Converts the given screen coordinates to real coordinates.

        @param pos: The screen coordinates to convert.
        @return: The real coordinates.
        """
        cx, cy, cz = self.CENTER_X, self.CENTER_Y, self.CENTER_Z;
        return Vector3(
            (pos.x - cx) / self.UNIVERSE_SCALE_FACTOR,
            (pos.y - cy) / -self.UNIVERSE_SCALE_FACTOR,
            (pos.z - cz) / self.UNIVERSE_SCALE_FACTOR,
        );


    def real_to_screen_coords(self, pos: Vector3):
        """
        Converts the given real coordinates to screen coordinates.

        @param pos: The real coordinates to convert.
        @return: The screen coordinates.
        """
        cx, cy, cz = self.CENTER_X, self.CENTER_Y, self.CENTER_Z;
        return Vector3(
            cx + pos.x * self.UNIVERSE_SCALE_FACTOR,
            cy + pos.y * -self.UNIVERSE_SCALE_FACTOR,
            cz + pos.z * self.UNIVERSE_SCALE_FACTOR,
        );


    def real_to_screen_radius(self, radius):
        """
        Converts the given real radius to screen radius.

        @param radius: The real radius to convert.
        @return: The screen radius.
        """
        return radius + self.UNIVERSE_SCALE_FACTOR;


    def render_debug_data(self):
        """
        Renders debug data to the screen.
        """
        def f(num):
            return num * self.UNIVERSE_SCALE_FACTOR;

        days_per_second = self.UNIVERSE_TIMESTEP / (60 * 60 * 24);

        text = self.font.render(f"FPS: {str(int(self.clock.get_fps()))}", True, (255, 255, 255));
        self.screen.blit(text, (10, 10));

        text = self.font.render(f"Mouse: {str(pygame.mouse.get_pos())}", True, (255, 255, 255));
        self.screen.blit(text, (10, 30));

        text = self.font.render(f"G: {str(self.G)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 50));

        text = self.font.render(f"Scale Factor: {str(self.UNIVERSE_SCALE_FACTOR)}", True, (255, 255, 255));
        self.screen.blit(text, (10, 70));

        text = self.font.render(f"Timestep: {self.UNIVERSE_TIMESTEP:,.5f} seconds/second,  {days_per_second:,.5f} days/second", True, (255, 255, 255));
        self.screen.blit(text, (10, 110));

        if(self.clock.get_fps() > 0):
            text = self.font.render(f"Time Elapsed: {str(self.ticks)} ticks, {(self.ticks / self.clock.get_fps() * days_per_second):,.5f} days", True, (255, 255, 255));
            self.screen.blit(text, (10, 130));

        if(self.selected_body):
            text = self.font.render(f"Selected Body: {self.selected_body.name} - M:{self.selected_body.mass}, P:{self.selected_body.position}", True, self.selected_body.color);
            self.screen.blit(text, (10, 150));

        return;


    def get_sun(self):
        return CelestialBody(self, "Sun", astropy.constants.M_sun.value, 20, P_sun, V_sun, C_sun);

    def get_mercury(self):
        return CelestialBody(self, "Mercury", M_mercury, 10, P_mercury, V_mercury, C_mercury);

    def get_venus(self):
        return CelestialBody(self, "Venus", M_venus, 10, P_venus, V_venus, C_venus);

    def get_earth(self):
        return CelestialBody(self, "Earth", astropy.constants.M_earth.value, 10, P_earth, V_earth, C_earth);

    def get_moon(self):
        return CelestialBody(self, "Moon", M_moon, 5, P_moon, V_moon, C_moon);

    def get_mars(self):
        return CelestialBody(self, "Mars", M_mars, 10, P_mars, V_mars, C_mars);

    def get_jupiter(self):
        return CelestialBody(self, "Jupiter", astropy.constants.M_jup.value, 12, P_jupiter, V_jupiter, C_jupiter);

    def get_saturn(self):
        return CelestialBody(self, "Saturn", M_saturn, 10, P_saturn, V_saturn, C_saturn);

    def get_uranus(self):
        return CelestialBody(self, "Uranus", M_uranus, 10, P_uranus, V_uranus, C_uranus);

    def get_neptune(self):
        return CelestialBody(self, "Neptune", M_neptune, 10, P_neptune, V_neptune, C_neptune);

    def get_pluto(self):
        return CelestialBody(self, "Pluto", M_pluto, 5, P_pluto, V_pluto, C_pluto);
