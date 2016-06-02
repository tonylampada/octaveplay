function [J, grad] = costFunction(theta, X, y, lambda)

m = length(y);
n = length(theta);
theta0 = [0; theta(2:n, 1)];
predictions = sigmoid(X * theta);
ytrans = y';
J = -(ytrans * log(predictions) + (1 - ytrans) * log(1 - predictions)) / m + (lambda * theta0' * theta0) / (2 * m);
grad = (X' * (predictions - y)) / m + lambda * theta0 / m;
end
