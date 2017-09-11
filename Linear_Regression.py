"""Simple Linear Regression using scipy and dataset from 
Kaggle (https://www.kaggle.com/andonians/random-linear-regression)"""
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

data = pd.read_csv("my_train_file_path")
x = data['x']
y = data['y']
x = np.array(x)
y = np.array(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
def predict(x):
    return slope * x + intercept
fitLine = predict(x)
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='b')
plt.show()
