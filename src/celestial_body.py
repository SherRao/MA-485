import simulation;
import pygame;

class CelestialBody:
    def __init__(self, simulation, mass, radius, position, velocity, acceleration, color):
        self.simulation = simulation;
        self.mass = mass;
        self.radius = radius;
        self.position = position;
        self.velocity = velocity;
        self.acceleration = acceleration;
        self.color = color;
        pass;

    def tick(self, bodies):
        for body in self.simulation.bodies:
            if (body != self):
                self.acceleration += self.get_gravitational_acceleration(body);
        self.velocity += self.acceleration;
        self.position += self.velocity;
        pass;

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius);
        pass;

    def dispose(self):
        pass;

    def get_gravitational_acceleration(self, body):
        distance = body.position - self.position;
        magnitude = distance.magnitude();
        direction = distance.normalize();
        return (direction * (simulation.Simulation.G * self.mass * body.mass / (magnitude ** 2)));

