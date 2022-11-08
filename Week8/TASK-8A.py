from sklearn.linear_model import LinearRegression
import seaborn as sns
iris = sns.load_dataset('iris')
import numpy as np
import matplotlib.pyplot as plt

sl = iris["sepal_length"]
sw = iris["sepal_width"]
pl = iris["petal_length"]
pw = iris["petal_width"]
species = iris["species"]

y = pl

# Petal Length vs Petal Width
x1 = np.array(pw).reshape(-1,1)
model_plvpw = LinearRegression(fit_intercept=True)
model_plvpw.fit(x1,y)
x1fit = np.linspace(0, 3)
X1fit = x1fit[:, np.newaxis]
y1fit = model_plvpw.predict(X1fit)
plt.scatter(x1, y)
plt.plot(x1fit, y1fit)
plt.show()
print("\nCoefficient and Intercept line for Petal Length vs Petal Width")
print(model_plvpw.coef_)
print(model_plvpw.intercept_)


# Petal Length vs Septal Width
x2 = np.array(sw).reshape(-1,1)
model_plvsw = LinearRegression(fit_intercept=True)
model_plvsw.fit(x2,y)
x2fit = np.linspace(2, 5)
X2fit = x2fit[:, np.newaxis]
y2fit = model_plvsw.predict(X2fit)
plt.scatter(x2, y)
plt.plot(x2fit, y2fit)
plt.show()
print("\nCoefficient and Intercept line for Petal Length vs Septal Width")
print(model_plvsw.coef_)
print(model_plvsw.intercept_)

# Petal Length vs Septal Length
x3 = np.array(sl).reshape(-1,1)
model_plvsl = LinearRegression(fit_intercept=True)
model_plvsl.fit(x3,y)
x3fit = np.linspace(4, 8)
X3fit = x3fit[:, np.newaxis]
y3fit = model_plvsl.predict(X3fit)
plt.scatter(x3, y)
plt.plot(x3fit, y3fit)
plt.show()
print("\nCoefficient and Intercept line for Petal Length vs Septal Length")
print(model_plvsl.coef_)
print(model_plvsl.intercept_)












