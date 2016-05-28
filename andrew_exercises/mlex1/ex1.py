import os
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
import itertools

FOLDER = os.path.dirname(os.path.realpath(__file__))


def load_data():
    datafile = FOLDER + '/ex1data1.txt'
    data = np.loadtxt(datafile, delimiter=',')
    y = data[:, 1:2]
    m = y.size
    X = np.hstack((np.ones((m, 1)), data[:, 0:1]))
    theta = np.zeros((2, 1))
    print('loaded %s training samples' % m)
    return X, y, theta


def compute_cost(X, y, th):
    diffs = X.dot(th) - y
    m = y.size
    return (1.0 / (2 * m)) * sum(np.multiply(diffs, diffs))[0]


def gradient_descent(X, y, th, alpha, num_iters):
    m = y.size
    J_hist = np.zeros((num_iters + 1, 1))
    th_hist = np.zeros((num_iters + 1, 2))
    J_hist[0, 0] = compute_cost(X, y, th)
    th_hist[0, :] = th.transpose()
    for i in range(num_iters):
        diffs = X.dot(th) - y
        delta = (1.0 / m) * (X.transpose().dot(diffs))
        th -= alpha * delta
        J_hist[i + 1, 0] = compute_cost(X, y, th)
        th_hist[i + 1, :] = th.transpose()
    return th, J_hist, th_hist


def plot_data(X, y):
    figure('fig1', figsize=(10, 6))
    plot(X[:, 1], y, 'rx', markersize=10)  # Mas olha, quem copiou quem??
    grid(True)
    ylabel('Profit in $10,000s')
    xlabel('Population of City in 10,000s')
    title('Raw data vs. linear approximation', fontsize=24)


def run_gradient_descent(X, y, theta):
    print 'The cost for theta=[0,0] is %s' % compute_cost(X, y, theta)
    alpha = 0.01
    num_iterations = 1500
    theta_opt, J_history, theta_hist = gradient_descent(X, y, theta, alpha, num_iterations)
    print 'Gradient descent got us this optimum theta: \n%s' % theta_opt
    return theta_opt, J_history, theta_hist


def plot_cost_convergence(J_history):
    figure('fig2', figsize=(10, 6))
    grid(True)
    ylabel(r'Cost - J($\theta$)')
    xlabel('num iterations')
    title('Cost convergence', fontsize=24)
    plot(J_history, 'bo-')


def plot_hipothesys_fit(X, theta_opt):
    figure('fig1')
    plot(X[:, 1:2], X.dot(theta_opt))


def plot_3d_cost(X, y, theta_hist, J_history):
    f3 = figure('fig3', figsize=(12, 12))
    ax = f3.gca(projection='3d')

    xvals = np.arange(-10, 10, .5)
    yvals = np.arange(-1, 4, .1)
    myxs, myys, myzs = [], [], []
    for th0 in xvals:
        for th1 in yvals:
            myxs.append(th0)
            myys.append(th1)
            myzs.append(compute_cost(X, y, np.matrix([[th0], [th1]])))

    xlabel(r'$\theta_0$', fontsize=30)
    ylabel(r'$\theta_1$', fontsize=30)
    title('Cost (Minimization Path Shown in Blue)', fontsize=30)
    scat = ax.scatter(myxs, myys, myzs, c=np.abs(myzs), cmap=get_cmap('YlOrRd'))
    plot(theta_hist[:, 0], theta_hist[:, 1], [j[0] for j in J_history], 'bo-')


if __name__ == '__main__':
    X, y, theta = load_data()
    plot_data(X, y)
    theta_opt, J_history, theta_hist = run_gradient_descent(X, y, theta)
    plot_cost_convergence(J_history)
    plot_hipothesys_fit(X, theta_opt)
    plot_3d_cost(X, y, theta_hist, J_history)
    show()
