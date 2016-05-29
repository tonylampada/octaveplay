import os
import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
import itertools

from numpy.lib.function_base import meshgrid

try:
    from andrew_exercises.mlex1 import ex1
except:
    import ex1


FOLDER = os.path.dirname(os.path.realpath(__file__))


def load_data():
    datafile = FOLDER + '/ex1data2.txt'
    data = np.loadtxt(datafile, delimiter=',')
    y = data[:, 2:3]
    m = y.size
    feats = data[:, 0:2]
    theta = np.zeros((3, 1))
    print('loaded %s training samples' % m)
    return feats, y, theta


def plot_data(X, y):
    f1 = figure('fig1', figsize=(10, 6))
    ax = f1.gca(projection='3d')
    grid(True)
    xlabel('size in square feet')
    ylabel('bedrooms')
    title('Raw data vs. linear approximation', fontsize=24)
    ax.scatter(X[:, 0], X[:, 1], y, c=np.abs(y), cmap=get_cmap('YlOrRd'))


def normalize_features(feats):
    mu = np.mean(feats, axis=0)
    sigma = np.std(feats, axis=0, ddof=1)
    normalized_X = np.hstack((np.ones((feats.shape[0], 1)), np.divide(feats - mu, sigma)))
    return normalized_X, mu, sigma


def run_gradient_descent(X, y, theta):
    print 'The cost for theta=[0,0] is %s' % ex1.compute_cost(X, y, theta)
    alpha = 0.5
    num_iterations = 10
    theta_opt, J_history, theta_hist = ex1.gradient_descent(X, y, theta, alpha, num_iterations)
    print 'Gradient descent got us this optimum theta: \n%s' % theta_opt
    return theta_opt, J_history, theta_hist


def predict_house_sample(theta, mu, sigma):
    normalized_x = np.divide(np.matrix('[1650, 3]') - mu, sigma)
    xi = np.hstack((np.matrix('[1]'), normalized_x))
    price = xi.dot(theta)[0,0]
    print('Predicted price for 1650 sqft, 3 bedrooms = %s' % price)


def plot_cost_convergence(J_history):
    figure('fig2', figsize=(10, 6))
    grid(True)
    ylabel(r'Cost - J($\theta$)')
    xlabel('num iterations')
    title('Cost convergence', fontsize=24)
    plot(J_history, 'bo-')


def plot_hipothesys_fit(feats, X, theta_opt):

    def _minmax(v1, v2):
        return min(v1), max(v1), min(v2), max(v2)

    f1 = figure('fig1')
    ax = f1.gca(projection='3d')
    minx, maxx, miny, maxy = _minmax(X[:, 1], X[:, 2])
    zi = np.matrix([
        [1, minx, miny],
        [1, minx, maxy],
        [1, maxx, miny],
        [1, maxx, maxy],
    ]).dot(theta_opt)
    zi = [z[0, 0] for z in zi]
    minf0, maxf0, minf1, maxf1 = _minmax(feats[:, 0], feats[:, 1])
    f0i = [minf0, minf0, maxf0, maxf0]
    f1i = [minf1, maxf1, minf1, maxf1]
    f0im, f1im = meshgrid(f0i, f1i)
    ax.plot_surface(f0im, f1im, zi)

if __name__ == '__main__':
    feats, y, theta = load_data()
    plot_data(feats, y)
    X, mu, sigma = normalize_features(feats)
    theta_opt, J_history, theta_hist = run_gradient_descent(X, y, theta)
    predict_house_sample(theta_opt, mu, sigma)
    plot_cost_convergence(J_history)
    plot_hipothesys_fit(feats, X, theta_opt)
    show()