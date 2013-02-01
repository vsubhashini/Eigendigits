% Machine Learning HomeWork 1 - Eigen Digits
% This puts together the pieces of the eigendigits hw

%%Init
clear; close all; clc

%% Setup parameters required
input_layer_size = 400; %20x20 Input images of Digits
num_labels = 10;	% 10 labels from 1 to 10

%%=============Loading and Sample Visualization

% Load Training Data
fprintf('Loading and Visualizing Data ... \n')

load('digits.mat'); % training data stored in arrays trainImages, trainLabels, testImages, testLabels
[f1 f2 junk samples ] = size(trainImages);
samples

trainImages=double(trainImages);

% Randomly select 25 data points to display
%rand_indices = randperm(samples)
sel = trainImages(:,:,1:25);
displayImages(sel);

fprintf('Program paused. Press enter to continue.\n');
pause;

%Part-2 -- compute and display eigendigits

%convert column features
K=500; %number of training images
sel = trainImages(:,:,1:K);

%Pick train images at random
permuted60k = randperm(size(trainImages,4));
%sel = trainImages(:, :, 1, permuted60k(1:K));
displayImages(sel);
fprintf('25 of K selected training images. Press enter to continue.\n');
pause;

A = reshape(sel,28*28,K);
[m V] = hw2FindEigendigits(A);

%display 25 eigendigits
Vreshaped = reshape(V,28,28,K);
displayImages(Vreshaped(:,:,1:25));

V_norm = matrixNormalize(V);

fprintf('Training images EigenDigits. Press enter to continue.\n');
pause;

%%==========Project Data into Eigenspace

trainZ = project2Eigen(V_norm, A, m);
test_rec = reconstruct(trainZ, V_norm, K);
rec_reshaped = reshape(test_rec,28,28,K);
displayImages(rec_reshaped(:,:,1:25));

fprintf('Training reconstruction. Program paused. Press enter to continue.\n');
pause;

%%==========Perform Testing

testSize=250;
testImages=double(testImages);
%selectTest = testImages(:,:,1:testSize);

%select test images randomly
%permuted60k = randperm(size(testImages,4));
permuted = randperm(5000);
%take 2nd half set (easy?)
%permuted = 5000+permuted;
selectTest = testImages(:, :, 1, permuted(1:testSize));
TestLabelSet = testLabels(1, permuted(1:testSize));

displayImages(selectTest);
fprintf('Test images. Program paused. Press enter to continue.\n');
pause;

%%===============Project Test Eigenvectors and reconstructed numbers

testA = reshape(selectTest,28*28,testSize);
testZ = project2Eigen(V_norm, testA, m);
test_rec = reconstruct(testZ, V_norm, K);
rec_reshaped = reshape(test_rec,28,28,testSize);
displayImages(rec_reshaped(:,:,1:25));

fprintf('Test Eigendigits. Program paused. Press enter to continue.\n');
pause;

%%==============Find k-nearest neighbours
%compare column distance
%label test set. K-nearest - 1-nearest neighbour
k=3;
min_dist_indices = knn(trainZ, testZ, k);

%%==============Classify (assign labels) based on knn

%assign labels based on indices
[myTestLabels fullLabs] = assignLabels(trainLabels, min_dist_indices);
accuracy = getAccuracy(myTestLabels, TestLabelSet);
accuracy

%%==============For generating report
%%==============Uncomment relevant portions of the loop
%fprintf('Starting Results.\n');
%pause;

%%==============Vary training size K, vary nearest neighbours k. 
%%==============Do 10 runs for each and report average accuracy
%%==============Test on the easy set 5k and the hard test 5k sets separately
%%==============Vary by number of eigenvectors considered

%% Initialization
%manyK = [25 35 50 75 100 150 200 300 400 500];% 
%manyK = [600 700 784 800 1000];
%knnk = [1 2 3 4 5 6 7 8 9];
%
%fprintf('\n\n ========== Starting results =========\n');
%
%manyK = [50 100 300 500 700 1000];
%%manyK=[5000];
%%eigvecs=5000;
%knnk = [2];
%neigs=[5 10 20 50];
%Results = [0 0 0 0 0]; %K(train-size) testSize k(nearest-neighbour) 0hard/5kEasy accuracy
%
%testSize=500;
%k=3;
%testImages=double(testImages);
%
%%fid = fopen ("myResults_vary_EigVecs.txt","w");
%
%for K=manyK,
%    for eigvecs=neigs,
%	fprintf(stdout, 'K=%d \n',K);
%	sel = trainImages(:,:,1:K);
%	A = reshape(sel,28*28,K);
%	[m V] = hw2FindEigendigits(A);
%	V=V(:,1:eigvecs);
%	V_norm = matrixNormalize(V);
%	trainZ = project2Eigen(V_norm, A, m);
%	for k=knnk,
%		%permuted60k = randperm(size(trainImages,4));
%		%sel = trainImages(:, :, 1, permuted60k(1:K));
%		%permuted = randperm(size(testImages,4));
%		for start=[0 5000],
%			totalAccuracy=0.0;
%			for iter=1:10,
%				permuted = randperm(5000);
%				permuted=start+permuted;
%				pickBegin=permuted(iter);
%				if(pickBegin+testSize > 5000+start),
%					pickBegin=1;
%				end;
%				selectTest = testImages(:, :, 1, permuted(1:testSize));
%				TestLabelSet = testLabels(1, permuted(1:testSize));
%%				selectTest = testImages(:, :, 1, permuted(pickBegin:pickBegin+testSize-1));
%%				TestLabelSet = testLabels(1, permuted(pickBegin:pickBegin+testSize-1));
%				testA = reshape(selectTest,28*28,testSize);
%				testZ = project2Eigen(V_norm, testA, m);
%				min_dist_indices = knn(trainZ, testZ, k);
%				[myTestLabels fullLabs] = assignLabels(trainLabels, min_dist_indices);
%				accuracy = getAccuracy(myTestLabels, TestLabelSet);
%				totalAccuracy += accuracy;
%			end;
%			avgAccuracy=totalAccuracy/10.0;
%			if (start==0),
%				testing='hard';
%			else,
%				testing='easy';
%			end;
%			fprintf('K=%d, k=%d, num-eigs=%d, Hardness=%s, accuracy=%f \n', K, k, eigvecs, testing, accuracy);
%			fprintf(fid, "K=%d, k=%d, num-eigs=%d, Hardness=%s, accuracy=%f \n", K, k, eigvecs, testing, accuracy);
%			res_vec = [K testSize k start avgAccuracy];
%			Results = [Results; res_vec];
%			fflush(fid);
%			fflush(stdout);
%		end;
%	end;
%    end;
%end;

%fclose(fid);

%save results.mat Results;


%%==============Create plots

%for K=manyK,
%	rowsK=Results(Results(:,1)==K,:);	%select rows where col1=K
%	for k=knnk,	
%		rowsKk=rowsK(rowsK(:,3)==k,:);	%further, select rows where col3=k
%		for start=[0 5000],
%			rowsFinal=rowsKk(rowsKk(:,4)==start,:);
%			XaxisK=rowsFinal(

