import pandas as pd
from scipy.sparse import data
from sklearn.cluster import MiniBatchKMeans

if __name__=="__main__":
    dataset = pd.read_csv(".\clase-analisis-multivariado\data\candy.csv")
    print(dataset.head(5))

X = dataset.drop('competitorname', axis = 1)
kmeans = MiniBatchKMeans(n_clusters = 4, batch_size = 8).fit(X)

print("Total de centros: ", len(kmeans.cluster_centers_))
print("="*64)
print(kmeans.predict(X)) #Lista del cluster asignado para cada valor

dataset['group'] = kmeans.predict(X)
print(dataset)

