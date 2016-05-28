function J = computeCostMulti(X, y, theta)
m = length(y); % number of training examples
diffs = X * theta - y;
J = (1/(2*m)) * sum(diffs .* diffs);
end
