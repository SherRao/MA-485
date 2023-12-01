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
            if (body != self):
                fx, fy = self.calculate_gravitation_atraction_with(body);
                total_fx += fx;
                total_fy += fy;

        self.velocity.x += total_fx / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.velocity.y += total_fy / self.mass * self.simulation.UNIVERSE_TIMESTEP;
        self.position.x += self.velocity.x * self.simulation.UNIVERSE_TIMESTEP;
        self.position.y += self.velocity.y * self.simulation.UNIVERSE_TIMESTEP;
        return;


    def calculate_gravitation_atraction_with(self, other_body):
        other_pos = other_body.position;
        dx = (other_pos.x - self.position.x);
        dy = (other_pos.y - self.position.y);
        d = math.sqrt(dx ** 2 + dy ** 2);

        mass = self.mass;
        other_mass = other_body.mass;

        f = self.simulation.G * self.mass * other_body.mass / d ** 2;
        theta = math.atan2(dy, dx);
        fx = math.cos(theta) * f;
        fy = math.sin(theta) * f;
        return fx, fy;


    # def update_gravitational_acceleration_with(self, other_body):
    #     other_pos = other_body.position;
    #     dx = other_pos.x - self.position.x;
    #     dy = other_pos.y - self.position.y;
    #     d = math.sqrt(dx ** 2 + dy ** 2);

    #     f = self.simulation.G * self.mass * other_body.mass / d ** 2;
    #     theta = math.atan2(dy, dx);
    #     fx = math.cos(theta) * f;
    #     fy = math.sin(theta) * f;

    #     self.velocity.x += fx / self.mass * self.simulation.UNIVERSE_TIMESTEP;
    #     self.velocity.y += fy / self.mass * self.simulation.UNIVERSE_TIMESTEP;
    #     self.position.x += self.velocity.x * self.simulation.UNIVERSE_TIMESTEP;
    #     self.position.y += self.velocity.y * self.simulation.UNIVERSE_TIMESTEP;

    #     scaledPosition = (self.position.x * self.simulation.UNIVERSE_SCALE_FACTOR, self.position.y * self.simulation.UNIVERSE_SCALE_FACTOR);
    #     self.travelledPath.append(scaledPosition);

        # fx = -(self.simulation.G * self.mass * other_body.mass * dx / r3);
        # fy = -(self.simulation.G * self.mass * other_body.mass * dy / r3);
        # vx = fx * dt / self.mass;
        # vy = fy * dt / self.mass;



    # def get_gravitational_acceleration(self, body: celestial_body.CelestialBody):
    #     other_pos = body.position;
    #     dx = other_pos.x - self.position.x;
    #     dy = other_pos.y - self.position.y;

    #     d = math.sqrt(dx ** 2 + dy ** 2);
    #     f = self.simulation.G * body.mass / d ** 2;
    #     theta = math.atan2(dx, dy);
    #     return Vector2(math.sin(theta) * f, math.cos(theta) * f);
    #     # distance = body.position - self.position;
    #     # magnitude = distance.magnitude();
    #     # direction = distance.normalize();
    #     # return (direction * (simulation.Simulation.G * self.mass * body.mass / (magnitude ** 2))) / self.mass;



    #     other_x, other_y = other.x, other.y
    #     distance_x = other_x - self.x
    #     distance_y = other_y - self.y
    #     distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    #     if other.sun:
    #         self.distance_to_sun = distance
    #     force = self.G * self.mass * other.mass / distance ** 2
    #     theta = math.atan2(distance_y, distance_x)
    #     force_x = math.cos(theta) * force
    #     force_y = math.sin(theta) * force
    #     return force_x, force_y
