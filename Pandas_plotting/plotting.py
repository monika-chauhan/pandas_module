import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data.plot()
plt.show()
