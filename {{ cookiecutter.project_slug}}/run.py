# run.py
from model import MoneyModel
from mesa.batchrunner import BatchRunner

batch_run = BatchRunner(
    MoneyModel,
    variable_parameters={"num_agents": range(10, 500, 10)},
    fixed_parameters={"width": 10, "height": 10},
    iterations=1,
    max_steps=100,
    model_reporters=None,  # {'agent_count': 'num'},
    agent_reporters=None,  # {'unique_id': 'unique_id', 'model': 'model'}
    display_progress=True)

batch_run.run_all()
