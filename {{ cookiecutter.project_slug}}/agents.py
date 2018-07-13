# model.py
from mesa import Agent
from mesa.time import RandomActivation


class BaseAgent(Agent):
    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)


class {{  cookiecutter.agent_name  }}(BaseAgent):
    """ An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        """One step"""
        pass
