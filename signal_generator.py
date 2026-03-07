import pandas as pd
import numpy as np

class SignalGenerator:
    def __init__(self, data):
        self.data = data

    def compute_signals(self):
        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['Close']
        signals['signal'] = 0.0
        signals['signal'][1:] = np.where(self.data['Close'][1:] > self.data['Close'][:-1], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()
        return signals

# Example usage:
# data = pd.read_csv('historical_data.csv') # Load historical trading data
# sg = SignalGenerator(data)
# signals = sg.compute_signals()