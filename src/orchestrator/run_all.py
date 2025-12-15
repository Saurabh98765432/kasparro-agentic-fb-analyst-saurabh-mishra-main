from agents.agent import Agent
from utils.helpers import helper_function

def main():
    agent = Agent("Agent1")
    print(agent.act())
    print(helper_function())

if __name__ == "__main__":
    main()

