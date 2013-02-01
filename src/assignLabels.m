function [L Lset] = assignLabels(trainLabels, ind)
% assign test sample's label given the ordered k nearest neighbour's indices (ind)
% pick label of the neighbour's indices and assign them to test data based on majority k-nearest

L=zeros(size(ind,1),1);
Lset=zeros(size(ind));

for i=1:size(ind,1),
	for j=1:size(ind,2),
		Lset(i,j) = trainLabels(1, ind(i,j));
	end;
	% count occurences of each unique element and pick maximum
	[u, junk, j] = unique(Lset(i,:));		%Gives unique elements
	[max_freq max_ind] = max([accumarray(j', 1)]);	%get frequency of unique elements, and get the index of max_freq element
	if (max_freq > 1),
		L(i) = u'(max_ind);			%Pick the maximum frequency element's label
	else,
		L(i) = Lset(i,1);			%if confused, pick nearest neighbour
	end;
end;

% replace below by majority of each row
%L = Lset(:,1);



end
