function [X_norm, meanMu] = inputNormalize(X)
% Function that normalizes each column (feature) in X
% 1. find mu=mean values for each column
% 2. subtract each value in X from the mean
% 3. find sigma=standard deviation of X (the range of values in X)
% 4. X_norm = (X-mean)/std-deviation
% Verify that, mean of X_norm is 0 and std deviation is 1. So values are in range -1 <= x <= 1

meanMu = mean(X);
X_norm = bsxfun(@minus, X, meanMu);

%stdSigma = std(X_norm);
%X_norm = bsxfun(@rdivide, X_norm, stdSigma);

end
