function accuracy = getAccuracy(myLabels, testLabels)
% compute the accuracy of the assigned labels in comparison to the testLabels

total = size(myLabels, 1);
accuracy=0.0;
match=0.0;

for i=1:total,
	if myLabels(i) == testLabels(1,i),
		match = match + 1.0;
	end;
end;

accuracy = double((match*100.0)/(double(total)*1.0));

end;
