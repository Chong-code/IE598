import sklearn
print( 'The scikit learn version is {}.'.format(sklearn.__version__))

from sklearn import datasets
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target
print( X_iris.shape, y_iris.shape)
print( X_iris[0], y_iris[0])

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

X, y = X_iris[:, :2], y_iris
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
print( X_train.shape, y_train.shape)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

import matplotlib.pyplot as plt
import matplotlib
colors = ['red', 'yellowgreen', 'blue']

for i in range(len(colors)):
    xs = X_train[:, 0][y_train == i]
    ys = X_train[:, 1][y_train == i]
    plt.scatter(xs, ys, c=colors[i])
    
plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, y_train)

print( clf.coef_)
print( clf.intercept_)

import numpy as np
x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5

Xs = np.arange(x_min, x_max, 0.5)
fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10, 6)
clist=['r','y','b']
for i in [0, 1, 2]:
    axes[i].set_aspect('equal')
    axes[i].set_title('Class '+ str(i) +' versus the rest')
    axes[i].set_xlabel('Sepal length')
    axes[i].set_ylabel('Sepal width')
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(y_min, y_max)
    
    plt.sca(axes[i])
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,cmap=matplotlib.colors.ListedColormap(clist))
    ys = (-clf.intercept_[i] - Xs * clf.coef_[i, 0]) / clf.coef_[i, 1]
    plt.plot(Xs, ys)
	
print( clf.predict(scaler.transform([[4.7, 3.1]])))

print( clf.decision_function(scaler.transform([[4.7, 3.1]])))

from sklearn import metrics
y_train_pred = clf.predict(X_train)
print( metrics.accuracy_score(y_train, y_train_pred))

y_pred = clf.predict(X_test)
print( metrics.accuracy_score(y_test, y_pred))

print( metrics.classification_report(y_test, y_pred, target_names=iris.target_names))

print( metrics.confusion_matrix(y_test, y_pred))

print("My name is Chong Zhao")
print("My NetID is: 657063491")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")
print("This code is a direct cite from Moncecchi, Guillermo and Raul Garreta. 2013. Learning scikit-learn: Machine Learning in Python. Packt Publishing. PP(10-18)")
