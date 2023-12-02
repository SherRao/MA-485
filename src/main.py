import pygame;
import simulation;

WIDTH, HEIGHT = (1920, 1080);
FPS = 120;

def main():
    pygame.init();
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT), display=1);
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

        keys_pressed = pygame.key.get_pressed();
        if keys_pressed[pygame.K_z]:
            sim.scale(1);
            print("Scale: ", sim.UNIVERSE_SCALE_FACTOR)

        if keys_pressed[pygame.K_x]:
            sim.scale(-1);
            print("Scale: ", sim.UNIVERSE_SCALE_FACTOR)


        screen.fill("black");
        sim.tick();
        sim.render();
        pygame.display.flip();
        clock.tick(FPS);

    pygame.quit();
    return;

if(__name__ == "__main__"):
    main();
