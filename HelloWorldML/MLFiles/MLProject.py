import numpy as np
from sklearn.linear_model import LinearRegression as lr
import pandas as pd
import matplotlib.pyplot as plt
class main():
    def __init__(self):
        super().__init__()
        dataset = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
        readdata()

def readdata():
    data = pd.read_csv("dataset.csv")
    x= data["m2"]
    y= data["price"]
    x= x.values.reshape(6,1)
    y=y.values.reshape(6,1)
    linear_regression(x,y)

def linear_regression(x,y):
    lineerreg  = lr()
    lineerreg.fit(x,y)
    lineerreg.predict(x)
    m=lineerreg.coef_
    b=lineerreg.intercept_
    plt.scatter(x, y)
    plt.plot(x,lineerreg.predict(x),c="red")
    plt.show()


main()