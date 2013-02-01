function Z = project2Eigen(V, A, mu)
%project (784 x Samples) data to (trainData x Samples) dimension eigenspace

Z = zeros(size(V,2), size(A,2));
A_norm = bsxfun(@minus, A, mu);
Z = V' * A_norm;

end
