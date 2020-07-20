import numpy as np


class Normalize:
    def ep(self, temperature):
        exp = np.exp((17.62 * temperature)/(temperature + 243.12))
        resp = 1.0044 * 6.112 * exp
        return resp
