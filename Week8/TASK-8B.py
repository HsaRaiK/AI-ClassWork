from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import image
from sklearn.cluster import KMeans
import seaborn as sns
iris = sns.load_dataset('iris')
import numpy as np
import matplotlib.pyplot as plt


sl = iris["sepal_length"]
sw = iris["sepal_width"]
pl = iris["petal_length"]
pw = iris["petal_width"]
species = iris["species"]
visitedarr = []
for a in species:
    if a not in visitedarr:
        visitedarr.append(a)

for a in visitedarr:
    print(a)

print(visitedarr.__len__())

x1 = np.array(pw).reshape(-1,1)
x2 = np.array(sw).reshape(-1,1)
x3 = np.array(sl).reshape(-1,1)
x4 = np.array(pl).reshape(-1,1)


plt.scatter(x1,x4)
plt.show()
plt.scatter(x1,x2)
plt.show()
plt.scatter(x1,x3)
plt.show()
plt.scatter(x2,x3)
plt.show()
plt.scatter(x2,x4)
plt.show()
plt.scatter(x3,x4)
plt.show()



