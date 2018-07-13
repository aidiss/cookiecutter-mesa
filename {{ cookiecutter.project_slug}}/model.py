from mesa.datacollection import DataCollector
from mesa.model import Model
from mesa.time import {{  cookiecutter.scheduler  }}

from agents import {{  cookiecutter.agent_name  }}


class MoneyModel(Model):
    """A model"""

    def __init__(self, *args, **kwargs):
        self.schedule = {{  cookiecutter.scheduler  }}(model=self)
        self.running = True
        self.datacollector = DataCollector()
 
        # Create agents
        for i in range(kwargs['num_agents']):
            a = {{  cookiecutter.agent_name  }}(i, self)
            self.schedule.add(a)

    def __repr__(self):
        return self.__class__.__name__

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()
