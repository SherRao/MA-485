import celestial_body;
import simulation;
import pygame;
import math;

from pygame import Vector2, Color;

class CelestialBody:
    def __init__(self, simulation, name: str, mass: float, radius: float, position: Vector2, velocity: Vector2, acceleration: Vector2, color: Color):
        self.simulation = simulation;
        self.name = name;
        self.mass = mass;
        self.radius = radius;
        self.position = position;
        self.velocity = velocity;
        self.acceleration = acceleration;
        self.color = color;
        self.travelledPath = [];
        pass;

    def tick(self, bodies: list):
        for body in self.simulation.bodies:
            if (body != self):
                self.acceleration += self.get_gravitational_acceleration(body);

        self.velocity += self.acceleration;
        self.position += self.velocity;
        self.travelledPath.append(self.position);
        pass;

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius);
        print(self.name, len(self.travelledPath));
        if(len(self.travelledPath) > 10):
            pygame.draw.lines(screen, self.color, False, self.travelledPath, 2);
        pass;

    def dispose(self):
        pass;

    def get_gravitational_acceleration(self, body: list):
        other_pos = body.position;
        dx = other_pos.x - self.position.x;
        dy = other_pos.y - self.position.y;

        d = math.sqrt(dx ** 2 + dy ** 2);
        f = self.simulation.G * body.mass / d ** 2;
        theta = math.atan2(dx, dy);
        return Vector2(math.sin(theta) * f, math.cos(theta) * f);
        # distance = body.position - self.position;
        # magnitude = distance.magnitude();
        # direction = distance.normalize();
        # return (direction * (simulation.Simulation.G * self.mass * body.mass / (magnitude ** 2))) / self.mass;



        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
