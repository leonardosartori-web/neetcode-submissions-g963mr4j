import numpy as np
from numpy.typing import NDArray
from typing import Tuple

class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        
        forward = x @ w + b
        y_hat = 1 / (1+np.exp(-forward))

        delta = (y_hat - y_true) * y_hat * (1-y_hat)
        dL_dw = np.round(delta*x, 5)
        dL_db = round(float(delta), 5)

        return (dL_dw, dL_db)


