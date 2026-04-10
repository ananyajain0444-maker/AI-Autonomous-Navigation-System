import pygame
import time
import os

CELL_SIZE = 30

def run_simulation(env, agent, path, goal):
    pygame.init()

    # Create images folder if not exists
    os.makedirs("images", exist_ok=True)

    screen = pygame.display.set_mode(
        (env.width * CELL_SIZE, env.height * CELL_SIZE)
    )

    pygame.display.set_caption("Autonomous Navigation Simulation")

    running = True
    clock = pygame.time.Clock()

    path_index = 0

    # Save initial grid screenshot
    pygame.image.save(screen, "images/grid.png")

    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw grid + obstacles
        for x in range(env.width):
            for y in range(env.height):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if env.grid[x][y] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), rect)

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        # Save path image (only once)
        if path_index == 0:
            for (px, py) in path:
                pygame.draw.rect(screen, (0, 0, 255),
                                 (px*CELL_SIZE, py*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.image.save(screen, "images/path.png")

        # Move agent
        if path_index < len(path):
            agent.move(path[path_index])
            path_index += 1
            time.sleep(0.1)

        # Draw agent
        ax, ay = agent.position
        pygame.draw.rect(screen, (0, 255, 0),
                         (ax*CELL_SIZE, ay*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw goal
        gx, gy = goal
        pygame.draw.rect(screen, (255, 0, 0),
                         (gx*CELL_SIZE, gy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Save final output when reached goal
        if agent.position == goal:
            pygame.image.save(screen, "images/final_output.png")

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()