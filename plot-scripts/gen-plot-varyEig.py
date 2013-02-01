#! /usr/bin/python
# read the file extract trainSize, accuracy

import numpy as np;
import matplotlib.pyplot as mpl;

file = open("myResults_vary_EigVecs.txt");
#file = open("top20myR-k-order.txt");

Xeasy5=[];
Yeasy5=[];
Xeasy10=[];
Yeasy10=[];
Xeasy20=[];
Yeasy20=[];
Xeasy50=[];
Yeasy50=[];
Xhard5=[];
Yhard5=[];
Xhard10=[];
Yhard10=[];
Xhard20=[];
Yhard20=[];
Xhard50=[];
Yhard50=[];
#Xhard=[];
#Yhard=[];
#K=50;
#Y.append(0);
for line in file:
	line=line.replace("=",",");
	columns = line.split(",");
	columns[9]=columns[9].replace(" \n","");
	#print columns;
	#outputfile.write(columns[1] + "\t" + columns[3] + "\t" + columns[7]);
	#if(columns[7]=="easy"):
	if(columns[5]=="5" and columns[7]=="easy" ):
		Xeasy5.append(columns[1]);
		Yeasy5.append(columns[9]);
	if(columns[5]=="10" and columns[7]=="easy" ):
		Xeasy10.append(columns[1]);
		Yeasy10.append(columns[9]);
	if(columns[5]=="20" and columns[7]=="easy" ):
		Xeasy20.append(columns[1]);
		Yeasy20.append(columns[9]);
	if(columns[5]=="50" and columns[7]=="easy" ):
		Xeasy50.append(columns[1]);
		Yeasy50.append(columns[9]);
	if(columns[5]=="5" and columns[7]=="hard" ):
		Xhard5.append(columns[1]);
		Yhard5.append(columns[9]);
	if(columns[5]=="10" and columns[7]=="hard" ):
		Xhard10.append(columns[1]);
		Yhard10.append(columns[9]);
	if(columns[5]=="20" and columns[7]=="hard" ):
		Xhard20.append(columns[1]);
		Yhard20.append(columns[9]);
	if(columns[5]=="50" and columns[7]=="hard" ):
		Xhard50.append(columns[1]);
		Yhard50.append(columns[9]);

file.close();
print Xeasy5;
print Yeasy5;
print Xeasy50;
print Yeasy50;

title="Eigenvectors vs Training Size vs Accuracy (Easy Test Set)";
xaxis="Training Size";
yaxis="Accuracy";
mpl.xlabel(xaxis);
mpl.ylabel(yaxis);
mpl.xticks([50, 100, 300, 500, 700, 1000], [50, 100, 300, 500, 700, 1000]);
mpl.yticks(range(0,100, 10));
mpl.grid(True, which="both", ls="-.");
mpl.title(title);
mpl.plot(Xeasy5, Yeasy5, marker='o', linestyle="-", color='r', label='eigens=5');
mpl.plot(Xeasy10, Yeasy10, marker='o', linestyle="-", color='g', label='eigens=10');
mpl.plot(Xeasy20, Yeasy20, marker='o', linestyle="-", color='b', label='eigens=20');
mpl.plot(Xeasy50, Yeasy50, marker='o', linestyle="-", color='m', label='eigens=50');
mpl.legend(loc=4);
mpl.xlim(0,1010);
mpl.ylim(0,100);
figname="TrainVsAcc-easy.png";
mpl.savefig(figname, bbox_inches=0);
mpl.clf();
#break;

#outputfile.close();
title="Eigenvectors vs Training Size vs Accuracy (Hard Test Set)";
xaxis="Training Size";
yaxis="Accuracy";
mpl.xlabel(xaxis);
mpl.ylabel(yaxis);
mpl.xticks([50, 100, 300, 500, 700, 1000], [50, 100, 300, 500, 700, 1000]);
mpl.yticks(range(0,100, 10));
mpl.grid(True, which="both", ls="-.");
mpl.title(title);
mpl.plot(Xhard5, Yhard5, marker='o', linestyle="-", color='r', label='eigens=5');
mpl.plot(Xhard10, Yhard10, marker='o', linestyle="-", color='g', label='eigens=10');
mpl.plot(Xhard20, Yhard20, marker='o', linestyle="-", color='b', label='eigens=20');
mpl.plot(Xhard50, Yhard50, marker='o', linestyle="-", color='m', label='eigens=50');
mpl.legend(loc=4);
mpl.xlim(0,1010);
mpl.ylim(0,100);
figname="TrainVsAcc-hard.png";
mpl.savefig(figname, bbox_inches=0);
mpl.clf();
#break;

#outputfile.close();

