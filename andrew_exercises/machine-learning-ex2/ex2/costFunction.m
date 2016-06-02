function [J, grad] = costFunction(theta, X, y)

m = length(y);
predictions = sigmoid(X * theta);
ytrans = y';
J = -(ytrans * log(predictions) + (1 - ytrans) * log(1 - predictions)) / m;
grad = (X' * (predictions - y)) / m;
end
