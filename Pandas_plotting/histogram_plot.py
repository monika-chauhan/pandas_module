import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('data.csv')

data['Duration'].plot(kind='hist')
plt.show()