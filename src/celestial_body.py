import celestial_body;
import simulation;
import pygame;
import math;

from pygame import Vector2, Color;

class CelestialBody:
    def __init__(self, simulation, name: str, mass: float, radius: float, position: Vector2, velocity: Vector2, color: Color):
        self.simulation = simulation;
        self.name = name;
        self.mass = mass;
        self.radius = radius;
        self.position = position;
        self.velocity = velocity;
        # self.acceleration = acceleration;
        self.color = color;
        self.travelledPath = [];
        return;

    def tick(self):
        self.update_position();
        self.travelledPath.append(self.position);
        return;

    def render(self, screen):
        x, y = self.simulation.real_to_screen_coords(self.position);
        r = self.radius;
        pygame.draw.circle(screen, self.color, (x, y), r);
        if(len(self.travelledPath) > 10):
            pygame.draw.lines(screen, self.color, False, self.travelledPath, 2);

        return;


    def dispose(self):
        return;


    def update_position(self):
        total_fx = 0;
        total_fy = 0;
        for body in self.simulation.bodies:
            if (body == self):
                continue;
            fx, fy = self.calculate_gravitation_atraction_with(body);
            total_fx += fx;
            total_fy += fy;

        self.velocity.x += total_fx / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.velocity.y += total_fy / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.position.x += self.velocity.x * self.simulation.UNIVERSE_TIMESTEP;
        self.position.y += self.velocity.y * self.simulation.UNIVERSE_TIMESTEP;
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
