function X_rec = reconstruct(Z, V, K)
% Reconstruct an approximate full dimension (784) vector of the given K dimention vector Z

X_rec = zeros(size(V,1),size(Z,2));
X_rec = V * Z;

end
