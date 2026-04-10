from src.environment import Environment
from src.agent import Agent
from src.path_planning import astar
from src.visualization import run_simulation

def main():
    env = Environment(20, 20)
    start = (0, 0)
    goal = (19, 19)

    agent = Agent(start)

    path = astar(env.grid, start, goal)

    run_simulation(env, agent, path, goal)

if __name__ == "__main__":
    main()