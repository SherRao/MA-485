import simulation;
import pygame;
import math;

from pygame import Vector2, Vector3, Color;

class CelestialBody:
    def __init__(self, simulation, name: str, mass: float, radius: float, position: Vector3, velocity: Vector3, color: Color):
        self.simulation = simulation;
        self.name = name;
        self.mass = mass;
        self.radius = radius;
        self.position = position;
        self.velocity = velocity;
        self.color = color;
        self.orbit_color = color - Color(50, 50, 50);
        self.orbital_path = [];
        return;


    def tick(self):
        self.update_position();

        # Prunes the array and keeps the last n elements.
        n = self.simulation.MAX_ORBITAL_PATH_LENGTH;
        if(len(self.orbital_path) > n):
            self.orbital_path = self.orbital_path[-n:-1];

        return;


    def render(self, screen):
        x, y, z = self.simulation.real_to_screen_coords(self.position);
        r = max(1, self.radius * (self.simulation.UNIVERSE_SCALE_FACTOR * 500000000))
        pygame.draw.circle(screen, self.color, (x, y), r);

        if(self.name != "Sun"):
            self.render_orbit(screen);
            print("ORBIT: ", self.orbital_path);
        # if(len(self.orbital_path) > 2):
        #     scaled_points = []
        #     for point in self.orbital_path:
        #         scaled_point = self.simulation.real_to_screen_coords(point);
        #         if(self.name == "Earth"):
        #             print(scaled_point)
        #         scaled_points.append((scaled_point.x, scaled_point.y));

        #     pygame.draw.lines(screen, self.orbit_color, False, scaled_points, 2)

        # for(i, point) in enumerate(self.orbital_path):
        #     if (i > 0):
        #         p = self.simulation.real_to_screen_coords(Vector3(point[0], point[1], 0));
        #         pygame.draw.circle(screen, self.orbit_color, (p.x, p.y) , 1);

        return;


    def update_position(self):
        total_fx = 0;
        total_fy = 0;
        for body in self.simulation.bodies:
            if(body == self):
                continue;
            fx, fy = self.calculate_gravitation_atraction_with(body);
            total_fx += fx;
            total_fy += fy;

        self.velocity.x += total_fx / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.velocity.y += total_fy / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.position.x += self.velocity.x * self.simulation.UNIVERSE_TIMESTEP;
        self.position.y += self.velocity.y * self.simulation.UNIVERSE_TIMESTEP;
        self.orbital_path.append(self.position);
        return;


    def calculate_gravitation_atraction_with(self, other_body):
        dx = other_body.position.x - self.position.x;
        dy = other_body.position.y - self.position.y;
        d = math.sqrt(dx ** 2 + dy ** 2);

        f = self.simulation.G * self.mass * other_body.mass / d ** 2;
        theta = math.atan2(dy, dx);
        fx = math.cos(theta) * f;
        fy = math.sin(theta) * f;
        return fx, fy;


    def render_orbit(self, screen):
        for(i, point) in enumerate(self.orbital_path):
            scaled_point = self.simulation.real_to_screen_coords(point);
            sx, sy, sz = scaled_point;
            pygame.draw.circle(screen, self.orbit_color, (sx, sy), 2);

        return;


    def contains_point(self, screen_coords):
        scaled_position = self.simulation.real_to_screen_coords(self.position);
        dx = (screen_coords[0] - scaled_position.x) ** 2 + (screen_coords[1] - scaled_position.y) ** 2;
        return dx <= self.radius ** 2;
