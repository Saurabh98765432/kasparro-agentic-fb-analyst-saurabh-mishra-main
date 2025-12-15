def test_sample():
    assert 1 + 1 == 2

def test_agent_act():
    from src.agents.agent import Agent
    agent = Agent("TestAgent")
    assert agent.act() == "TestAgent is acting"
