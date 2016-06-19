import os
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
import itertools
import scipy.optimize as op
import collections


FOLDER = os.path.dirname(os.path.realpath(__file__))


def load_data():
    datafile = FOLDER + '/ex2data1.txt'
    data = np.loadtxt(datafile, delimiter=',')
    y = data[:, 2:3]
    m = y.size
    X = np.hstack((np.ones((m, 1)), data[:, 0:2]))
    theta = np.zeros((3, 1))
    print('loaded %s training samples' % m)
    return X, y, theta


def plot_data(X, y):
    Xneg = np.array([xi for xi, yi in zip(X, y) if yi[0] == 0])
    Xpos = np.array([xi for xi, yi in zip(X, y) if yi[0] == 1])
    figure('fig1', figsize=(10, 6))
    plot(Xneg[:, 1], Xneg[:, 2], 'rx', markersize=10)
    plot(Xpos[:, 1], Xpos[:, 2], 'bo', markersize=10)
    grid(True)
    ylabel('Grade 2')
    xlabel('Grade 1')
    legend('Admitted', 'Not admitted')
    title('Grades vs. Approval', fontsize=24)


def plot_decision_boundary(X, theta):
    t0, t1, t2 = theta

    def y0(x):
        return -(t0 + t1 * x) / t2

    minx, maxx = min(X[:, 1]), max(X[:, 1])
    xs = [minx, maxx]
    ys = [y0(x) for x in xs]
    figure('fig1')
    plot(xs, ys, 'b--')
    pass


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost_function(X, y):
    m, n = X.shape
    ytrans = y.transpose()

    def _cost(theta):
        theta = theta.reshape((n, 1))
        predictions = sigmoid(X.dot(theta))
        J = -(ytrans.dot(np.log(predictions)) + (1 - ytrans).dot(np.log(1 - predictions))) / m
        return J
    return _cost


def grad_func(X, y):
    m, n = X.shape

    def _grad(theta):
        theta = theta.reshape((n, 1))
        predictions = sigmoid(X.dot(theta))
        grad = (X.transpose().dot(predictions - y)) / m
        return grad

    return _grad


def get_accuracy(X, y, theta):
    m, n = X.shape
    theta = theta.reshape(n, 1)
    predictions = X.dot(theta) >= 0
    reality = y == 1
    rights = predictions == reality
    counter = collections.Counter(rights.reshape(m))
    count_rights = counter[True]
    accuracy = float(count_rights) / m
    return accuracy


if __name__ == '__main__':
    X, y, theta = load_data()
    plot_data(X, y)
    init_theta = np.zeros((3, 1))
    _cost = cost_function(X, y)
    _grad = grad_func(X, y)
    J0 = _cost(init_theta)
    theta_opt = op.minimize(fun=cost_function(X, y),
                            x0=init_theta,
                            method='TNC',
                            jac=grad_func(X, y)).x
    Jmin = _cost(theta_opt)
    accuracy = get_accuracy(X, y, theta_opt)
    plot_decision_boundary(X, theta_opt)
    show()x
    print('cost at (0,0,0) is %s' % J0[0][0])
    print('optimum theta is %s' % theta_opt)
    print('cost at theta_min = %s' % Jmin[0][0])
    print('Accuracy is %s' % accuracy)
