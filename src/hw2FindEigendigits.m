function [m V] = hw2FindEigendigits(A)
%PCA partial by creating Eigendigits
% [m V] = hw2FindEigendigits(A) computes the mean m of matrix A
%         and V the eigenvectors of the covariance matrix

% get the number of rows (features) and the columns (number of training samples) of the input matrix
[r c] = size(A);

%Normalize the matrix X before getting eigenvalues/vectors
%reshape A to columns (i.e make features in columns and then send to normalize)
[A_norm, meanMu] = inputNormalize(A');
A_norm = A_norm'*1.0;
m = meanMu';

% Get covariance matrix for reduced k*k using notes
% Actual co-var = 1/m sum(X*X'); remember that X*X' has rank just 1. Therefore, rank of co-var-mat is only M (number of samples)
% So, compute eigen vector for reduced matrix instead of for the full co-var 
% A'*Av = mu V where V is eigenvector , mu - eigen value, A is m*(n^2) matrix, therefore A'*A is m^2
% To compute eigenvector of co-var matrix do mu * A * V

[U mu] = eig(A_norm'*A_norm);
V = A_norm*U;

%make V normalized norm(V:,1) =1
%sort eigenvalues in descending order

mu_sum = sum(mu);
[sorted sortIndex] = sort(mu_sum);
V = V(:,sortIndex(end:-1:1));

%Instead of considering all eigenvectors consider top t_eigvecs eigenvectors
%if (t_eigvecs==Inf),
%	V=V;
%else,
%	V=V(:,1:t_eigvecs);
