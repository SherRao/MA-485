import astropy.constants;
import pygame;
import scipy;

from celestial_body import CelestialBody;
from pygame import Vector3, Color;
from constants import *;

class Simulation:
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
        self.screen = screen;
        self.clock = clock;
        self.running = True;
        self.bodies = [];
        self.font = pygame.font.SysFont("Consolas", 18);
        self.debug = True;
        self.ticks = 0;
        self.selected_body = None;

        # sun
        self.bodies.append(CelestialBody(
            self,
            "Sun",
            astropy.constants.M_sun.value,
            20, #astropy.constants.R_sun.value * self.UNIVERSE_SCALE_FACTOR,
            Vector3(0, 0, 0),
            Vector3(0, 0, 0),
            Color(253, 184, 19)
        ));

        # # mercury
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Mercury",
        #     3.285e23, #astropy.constants.M_mercury.value,
        #     10, # astropy.constants.R_mercury.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(5.791e10, 0, 0),
        #     Vector3(0, 47.362e3, 0),
        #     Color(184, 184, 184)
        # ));

        # # venus
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Venus",
        #     4.867e24,#astropy.constants.M_venus.value,
        #     10, # astropy.constants.R_venus.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(1.082e11, 0, 0),
        #     Vector3(0, 35.02e3, 0),
        #     Color(184, 184, 184)
        # ));

        # earth
        self.bodies.append(CelestialBody(
            self,
            "Earth",
            astropy.constants.M_earth.value,
            10, # astropy.constants.R_earth.value * self.UNIVERSE_SCALE_FACTOR,
            Vector3(1.496e11, 0, 0),
            Vector3(0, 29.783e3, 0),
            Color(40, 122, 184)
        ));

        # moon
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Moon",
        #     7.34767309e22, #astropy.constants.M_moon.value,
        #     5, # astropy.constants.R_moon.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(1.496e11 + 3.844e8, 0, 0),
        #     Vector3(0, 29.783e3 + 1.022e3, 0),
        #     Color(184, 184, 184)
        # ));

        # # mars
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Mars",
        #     6.39e23, #astropy.constants.M_mars.value,
        #     10, # astropy.constants.R_mars.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(2.279e11, 0, 0),
        #     Vector3(0, 24.077e3, 0),
        #     Color(184, 40, 40)
        # ));

        # # jupiter
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Jupiter",
        #     astropy.constants.M_jup.value,
        #     12, # astropy.constants.R_jup.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(7.785e11, 0, 0),
        #     Vector3(0, 13.07e3, 0),
        #     Color(156, 63, 48)
        # ));

        # # saturn
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Saturn",
        #     5.683e26, #astropy.constants.M_saturn.value,
        #     10, # astropy.constants.R_saturn.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(1.433e12, 0, 0),
        #     Vector3(0, 9.69e3, 0),
        #     Color(184, 156, 48)
        # ));

        # # uranus
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Uranus",
        #     8.681e25, # astropy.constants.M_uranus.value,
        #     10, # astropy.constants.R_uranus.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(2.877e12, 0, 0),
        #     Vector3(0, 6.81e3, 0),
        #     Color(40, 184, 184)
        # ));

        # # neptune
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Neptune",
        #     1.024e26, #astropy.constants.M_neptune.value,
        #     10, # astropy.constants.R_neptune.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(4.495e12, 0, 0),
        #     Vector3(0, 5.43e3, 0),
        #     Color(40, 40, 184)
        # ));

        # # pluto
        # self.bodies.append(CelestialBody(
        #     self,
        #     "Pluto",
        #     1.309e22, #astropy.constants.M_pluto.value,
        #     5, # astropy.constants.R_pluto.value * self.UNIVERSE_SCALE_FACTOR,
        #     Vector3(5.906e12, 0, 0),
        #     Vector3(0, 4.67e3, 0),
        #     Color(184, 184, 184)
        # ));

        return;

    def tick(self):
        self.check_events();
        for body in self.bodies:
            body.tick();

        self.ticks += 1;
        return;


    def render(self):
        for body in self.bodies:
            body.render(self.screen);

        if(self.debug):
            self.render_debug_data();

        points = [(10, 10), (11, 11), (12, 12), (50, 50), (100, 100)];
        pygame.draw.lines(self.screen, Color(255, 0, 0), False, points, 1);
        return;


    def check_events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False;

            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.check_for_planet_selection();

            # if(event.type == pygame.MOUSEBUTTONDOWN):
            #     if(event.button == LEFT_MOUSE_BUTTON):
            #         self.drag = True;
            #         self.drag_start = pygame.mouse.get_pos();
            #         pygame.mouse.set_visible(False);

            # if(event.type == pygame.MOUSEBUTTONUP):
            #     if(event.button == LEFT_MOUSE_BUTTON):
            #         self.drag = False;
            #         self.drag_start = None;
            #         pygame.mouse.set_visible(True);

            # if(event.type == pygame.MOUSEMOTION):
            #     if(self.drag):
            #         dx = pygame.mouse.get_pos()[0] - self.drag_start[0];
            #         dy = pygame.mouse.get_pos()[1] - self.drag_start[1];
            #         self.pan_camera(dx, dy);
            #         self.drag_start = pygame.mouse.get_pos();


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
        mouse_pos = pygame.mouse.get_pos();
        for body in self.bodies:
            if(body.contains_point(mouse_pos)):
                print("Selected: ", body.name);
                self.selected_body = body;
                break;

        return;


    def scale(self, factor):
        future_scale = self.UNIVERSE_SCALE_FACTOR + (factor / self.AU);
        if(future_scale > 0):
            self.UNIVERSE_SCALE_FACTOR = future_scale;
        return;


    def pan_camera(self, dx=0, dy=0):
        self.CENTER_X += dx;
        self.CENTER_Y += dy;
        self.CENTER_Z += 0;
        return;


    def timestep(self, factor):
        self.DAYS_PER_SECOND = max(1/86400, self.DAYS_PER_SECOND - (.05 * factor));
        self.UNIVERSE_TIMESTEP = (60 * 60 * 24) * self.DAYS_PER_SECOND;
        return;


    def screen_to_real_coords(self, pos: Vector3):
        cx, cy, cz = self.CENTER_X, self.CENTER_Y, self.CENTER_Z;
        return Vector3(
            (pos.x - cx) / self.UNIVERSE_SCALE_FACTOR,
            (pos.y - cy) / -self.UNIVERSE_SCALE_FACTOR,
            (pos.z - cz) / self.UNIVERSE_SCALE_FACTOR,
        );


    def real_to_screen_coords(self, pos: Vector3):
        cx, cy, cz = self.CENTER_X, self.CENTER_Y, self.CENTER_Z;
        return Vector3(
            cx + pos.x * self.UNIVERSE_SCALE_FACTOR,
            cy + pos.y * -self.UNIVERSE_SCALE_FACTOR,
            cz + pos.z * self.UNIVERSE_SCALE_FACTOR,
        );


    def real_to_screen_radius(self, radius):
        return radius + self.UNIVERSE_SCALE_FACTOR;


    def render_debug_data(self):
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
