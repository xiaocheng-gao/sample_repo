from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
y = iris.target

print(X)
print(y)
print(X, y)

plt.plot(X)
plt.plot(y)