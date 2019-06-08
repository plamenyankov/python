import pandas as pd
import numpy as np
import timeit

s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())
print(len(s))

%%timeit -n 100
summary = np.sum(s)
%   
