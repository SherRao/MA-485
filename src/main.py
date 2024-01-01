import pygame;
import simulation;

WIDTH, HEIGHT = (1366, 768);
FPS = 120;

def main():
    """
    Main entry function - initializes pygame and starts the simulation.
    """
    pygame.init();
    pygame.mouse.set_cursor(*pygame.cursors.arrow);
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT));
    clock = pygame.time.Clock();
    sim = simulation.Simulation(screen, clock);

    while(sim.running):
        screen.fill("black");
        sim.tick();
        sim.render();

        clock.tick(FPS);
        pygame.display.flip();

    pygame.quit();
    return;


if(__name__ == "__main__"):
    main();
