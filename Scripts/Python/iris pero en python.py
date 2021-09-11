import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import mean
from sklearn.cluster import MeanShift
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans
from sklearn import datasets







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
#plt.show()


# Meanshift para iris

if __name__ == "__main__":
    iris = datasets.load_iris()
    dataset = iris

    meanshift = MeanShift().fit(X)
    print(meanshift.labels_)    
    print(len(meanshift.labels_))
    print("="*64)
    print(meanshift.cluster_centers_)

    dataset['meanshift'] = meanshift.labels_
    print("="*64)
    print(dataset)

    print("="*64 + "\n Componentes principales \n" + "="*64)
    pca = PCA(n_components = 2)
    pca.fit(X)

    pca_data = pca.transform(X)
    print(pca_data)

    print("="*64 + "\n MeanShift de PCA \n" + "="*64)
    meanshift = MeanShift().fit(pca_data)

    plt.scatter(pca_data[:, 0], 
                pca_data[:, 1],
                c = meanshift.predict(pca_data))
    plt.scatter(meanshift.cluster_centers_[:, 0], 
                meanshift.cluster_centers_[:, 1],
                c = [ 'purple','yellow'],
                s = 200)
    plt.show() 
    # No se porque sale una gráfica con 5 colores diferentes pero solo me marca 2 centro para los clusters 


    
