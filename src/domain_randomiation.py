# used in simrocketenv.py to introduce randomness in the simulation

import numpy as np

class DomainRandomisation:
    def __init__(self):
        self.params = {
            'gravity': {
                'range': (4.9, 14.7),
                'type': 'uniform'
            },
            'thrust_max_n': {
                'range': (1200, 1800),
                'type': 'uniform'
            },
            'initial_position': {
                'range': ((-100.0, 100.0), (-100.0, 100.0), (30.0, 100.0)),
                'type': 'uniform'
            },
            'wind_force': {
                'mean': 0,
                'std': 10,
                'type': 'normal'
            },
            'sensor_noise': {
                'mean': 0,
                'std': 0.01,
                'type': 'normal'
            },
            'actuator_noise': {
                'mean': 0,
                'std': 0.05,
                'type': 'normal'
            }
        }

    def get_randomized_value(self, param_name):
        param = self.params[param_name]
        if param['type'] == 'uniform':
            return np.random.uniform(*param['range'])
        elif param['type'] == 'normal':
            return np.random.normal(param['mean'], param['std'])
        else:
            raise ValueError(f"Unknown randomization type for {param_name}")

    def get_randomized_position(self):
        return np.array([
            self.get_randomized_value('initial_position')[0],
            self.get_randomized_value('initial_position')[1],
            self.get_randomized_value('initial_position')[2]
        ])

    def get_wind_force(self):
        return np.random.normal(
            self.params['wind_force']['mean'],
            self.params['wind_force']['std'],
            3
        )

    def get_noise(self, param_name, shape):
        param = self.params[param_name]
        return np.random.normal(param['mean'], param['std'], shape)