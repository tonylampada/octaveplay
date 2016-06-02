function p = predict(theta, X)
p = sigmoid(X * theta) >= 0.5;
end
