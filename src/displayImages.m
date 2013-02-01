function displayImages(sel)
%Pick the first 25 images to display. Arrange it in a 5x5 box

combinedImage=zeros(28*5, 28*5);
for i=1:5,
	for j=1:5,
		combinedImage(1+(i-1)*28:i*28, 1+(j-1)*28:j*28) = sel(:,:,((i-1)*5+j));
	end;
end;
imshow(combinedImage);

end
