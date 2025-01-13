import numpy as np
import matplotlib.pyplot as plt

# x = np.random.uniform(0.0, 5.0, 10000)
# plt.hist(x, 100)
# plt.show()

# y = np.random.normal(5.0, 1.0, 100000)
# plt.hist(y, 50)
# plt.show()
# x = np.random.normal(5.0, 1.0, 1000)
# y = np.random.normal(10.0, 2.0, 1000)
# plt.scatter(x, y)
# plt.show()

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data.csv", sep='\t')

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
