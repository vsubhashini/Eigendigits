#! /usr/bin/python
# read the file extract trainSize, accuracy

import numpy as np;
import matplotlib.pyplot as mpl;

file = open("results-full-Korder.txt");
#file = open("top20myR.txt");

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
		mpl.xlabel(xaxis);
		mpl.ylabel(yaxis);
		mpl.yticks(range(0,100, 10));
		mpl.xticks(range(0,10));
		mpl.grid(True, which="both", ls="-.");
		mpl.title(title);
		mpl.plot(Xeasy, Yeasy, marker='o', linestyle="-", color='r', label='EasyTest');
		mpl.plot(Xhard, Yhard, marker='o', linestyle="-", color='g', label='HardTest');
		mpl.legend(loc=4);
		mpl.xlim(0,10);
		mpl.ylim(0,100);
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

title="Number of nearest neighbours vs Accuracy (training Size = " + str(K) +" )";
xaxis="k of k-nearest neighbours";
yaxis="accuracy";
mpl.xlabel(xaxis);
mpl.ylabel(yaxis);
mpl.yticks(range(0,100, 10));
mpl.xticks(range(0,10));
mpl.grid(True, which="both", ls="-.");
mpl.title(title);
mpl.plot(Xeasy, Yeasy, marker='o', linestyle="-", color='r', label='EasyTest');
mpl.plot(Xhard, Yhard, marker='o', linestyle="-", color='g', label='HardTest');
mpl.legend(loc=4);
mpl.xlim(0,10);
mpl.ylim(0,100);
figname="knnVsAcc-K-"+ str(K) +".png";
mpl.savefig(figname, bbox_inches=0);
Xeasy=[];
Yeasy=[];
Xhard=[];
Yhard=[];
K=columns[1];
mpl.clf();
#outputfile.close();
