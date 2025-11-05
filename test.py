from sklearn.datasets import fetch_openml
from sklearn.model_selection import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


mnist = fetch_openml('mnist_784', as_frame=False)

X = mnist.data
y = mnist.target

x_train, y_train = X[:60000], y[:60000]
x_test, y_test = X[60000:], y[60000:]

weights = ["distance", "uniform"]

results = []
for w in weights:
    for i in range(1, 10): 
      print(f'{i} for {w}')
      kn_clf = KNeighborsClassifier(n_neighbors=i, weights=w)
      results.append(cross_val_score(kn_clf, x_train, y_train, cv=3))

print(results)
