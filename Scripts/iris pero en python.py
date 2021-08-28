from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

#Hagamos un gráfico

xmin, xmax = X[:, 0].min() - 0.5, X[:, 0].min() + 0.5
ymin, ymax = X[:, 1].min() - 0.5, X[:, 1].min() + 0.5

plt.figure(2, figsize = (8,9))
plt.clf()
plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.Set1, 
        edgecolors= 'k')
plt.show()