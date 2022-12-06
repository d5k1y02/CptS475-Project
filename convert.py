import numpy as np
import pandas as pd 

data = np.load('bodmas.npz')
frame = pd.DataFrame(data['X'])
frame.insert(2381, 'class', data['y'])
frame.to_csv("bodmas.csv")
