#! /usr/bin/python
# read the file extract trainSize, accuracy

import numpy as np;
import matplotlib.pyplot as mpl;

file = open("results-full-k-order.txt");
#file = open("top20myR-k-order.txt");

Xeasy=[];
Yeasy=[];
Xhard=[];
Yhard=[];
k=1;
#Y.append(0);
for line in file:
	line=line.replace("=",",");
	columns = line.split(",");
	#print columns;
	columns[7]=columns[7].replace(" \n","");
	#outputfile.write(columns[1] + "\t" + columns[3] + "\t" + columns[7]);
	if(columns[3]!=k):
		title="Training Size vs Accuracy (knn = " + str(k) +" )";
		xaxis="Training Size";
		yaxis="Accuracy";
		mpl.xlabel(xaxis);
		mpl.ylabel(yaxis);
		mpl.xticks([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]);
		mpl.yticks(range(0,100, 10));
		mpl.grid(True, which="both", ls="-.");
		mpl.title(title);
		mpl.plot(Xeasy, Yeasy, marker='o', linestyle="-", color='r', label='EasyTest');
		mpl.plot(Xhard, Yhard, marker='o', linestyle="-", color='g', label='HardTest');
		mpl.legend(loc=4);
		mpl.xlim(0,1010);
		mpl.ylim(0,100);
		figname="TrainVsAcc-k-"+ str(k) +".png";
		mpl.savefig(figname, bbox_inches=0);
		Xeasy=[];
		Yeasy=[];
		Xhard=[];
		Yhard=[];
		k=columns[3];
		mpl.clf();
		#break;
	if(columns[3]==k and columns[5]=="easy" ):
		Xeasy.append(columns[1]);
		Yeasy.append(columns[7]);
	if(columns[3]==k and columns[5]=="hard" ):
		Xhard.append(columns[1]);
		Yhard.append(columns[7]);

file.close();
#outputfile.close();

title="Training Size vs Accuracy (knn = " + str(k) +" )";
xaxis="Training Size";
yaxis="Accuracy";
mpl.xlabel(xaxis);
mpl.ylabel(yaxis);
mpl.xticks([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]);
mpl.yticks(range(0,100, 10));
mpl.grid(True, which="both", ls="-.");
mpl.title(title);
mpl.plot(Xeasy, Yeasy, marker='o', linestyle="-", color='r', label='EasyTest');
mpl.plot(Xhard, Yhard, marker='o', linestyle="-", color='g', label='HardTest');
mpl.legend(loc=4);
mpl.xlim(0,1010);
mpl.ylim(0,100);
figname="TrainVsAcc-k-"+ str(k) +".png";
mpl.savefig(figname, bbox_inches=0);
Xeasy=[];
Yeasy=[];
Xhard=[];
Yhard=[];
k=columns[3];
mpl.clf();
