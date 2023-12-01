import pygame;
import simulation;

SCREEN_WIDTH = 1280;
SCREEN_HEIGHT = 720;
FPS = 120;

def main():
    pygame.init();
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), display=1);
    clock = pygame.time.Clock();
    running = True;
    sim = simulation.Simulation(screen, clock, running);

    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False;

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    running = False;

                if(event.key == pygame.K_p):
                    sim.debug = not sim.debug;
                    print("Debug: ", sim.debug);

        screen.fill("black");
        sim.tick();
        sim.render();
        pygame.display.flip();
        clock.tick(FPS);

    pygame.quit();
    return;

if(__name__ == "__main__"):
    main();
