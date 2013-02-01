#! /usr/bin/python
# read the file extract trainSize, accuracy

import numpy as np;
import matplotlib.pyplot as mpl;

#file = open("myResultsto500.txt");
file = open("top20myR.txt");

Xeasy=[];
Yeasy=[];
Xhard=[];
Yhard=[];
K=25;
#Y.append(0);
for line in file:
	line=line.replace("=",",");
	columns = line.split(",");
	#print columns;
	columns[7]=columns[7].replace(" \n","");
	#outputfile.write(columns[1] + "\t" + columns[3] + "\t" + columns[7]);
	if(columns[1]!=K):
		title="Number of nearest neighbours vs Accuracy (training Size = " + str(K) +" )";
		xaxis="k of k-nearest neighbours";
		yaxis="accuracy";
		mpl.plot(Xeasy, Yeasy, marker='o', linestyle="-", color='r', label='EasyTest');
		mpl.plot(Xhard, Yhard, marker='o', linestyle="-", color='g', label='HardTest');
		mpl.xlabel(xaxis);
		mpl.ylabel(yaxis);
		mpl.title(title);
		mpl.legend();
		mpl.xlim(0,10);
		figname="knnVsAcc-K-"+ str(K) +".png";
		mpl.savefig(figname, bbox_inches=0);
		Xeasy=[];
		Yeasy=[];
		Xhard=[];
		Yhard=[];
		K=columns[1];
		mpl.clf();
		#break;
	if(columns[1]==K and columns[5]=="easy" ):
		Xeasy.append(columns[3]);
		Yeasy.append(columns[7]);
	if(columns[1]==K and columns[5]=="hard" ):
		Xhard.append(columns[3]);
		Yhard.append(columns[7]);

file.close();
#outputfile.close();
