function [N] = knn(X, S, k)
% A function that returns the index of the k nearest neighbours of a sample S in
%	among the points in X.
% Assume sample S is a column vector. Assume each column in X is a point.
%
% Check that S is in the same dimension as a point in X
size(S,1) - size(X,1); %=0?

%For k=1 (1 nearest neighbour)
%compute distance of S from each point in X
for i=1:size(S,2),	%for every point in S
	s = S(:,i);	% get point
	s_full = repmat(s,1,size(X,2));
	dists = sum((X-s_full).^2);
	[min_dists min_indices] = sort(dists);
	N(i,:) = min_indices;
end

% Find k  minimum dists and index/indices of min-dist points. Put the indices in a vector/matrix N
N = N(:,1:k);

end
