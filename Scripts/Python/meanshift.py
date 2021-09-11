from numpy.core.fromnumeric import mean
import pandas as pd
from sklearn.cluster import MeanShift
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    dataset = pd.read_csv(".\data\candy.csv")
    print(dataset.head(5))

    X = dataset.drop('competitorname', axis=1)
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

    print("="*64 + "\n MakeShift de PCA \n" + "="*64)
    meanshift = MeanShift().fit(pca_data)

    plt.scatter(pca_data[:, 0], 
                pca_data[:, 1],
                c = meanshift.predict(pca_data))
    plt.scatter(meanshift.cluster_centers_[:, 0], 
                meanshift.cluster_centers_[:, 1], 
                c = ['purple', 'cyan', 'yellow'],
                s = 200)
    plt.show()
    