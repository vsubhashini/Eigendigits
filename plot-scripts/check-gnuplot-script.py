#! /usr/bin/python
# read the file extract trainSize, accuracy

import Gnuplot;

file = open("myResultsto500.txt");
outputfile = open("check-out.txt","w");
#outputfile.write("#K-trainSize k-neighbours accuracy \n");

X=[];
Y=[];
#Y.append(0);
for line in file:
	line=line.replace("=",",");
	columns = line.split(",");
	#print columns;
	columns[7]=columns[7].replace(" \n","");
	#outputfile.write(columns[1] + "\t" + columns[3] + "\t" + columns[7]);
	if(columns[1]=="25" and columns[5]=="easy" ):
		X.append(columns[3]);
		Y.append(columns[7]);
		#print Y;
	if(columns[1]!="25"):
		gp = Gnuplot.Gnuplot();
		title="Number of nearest neighbours vs Accuracy (training Size = " + "25" +" )";
		gp('set term png small');
		gp.title(title);
		xaxis="k-nearest neighbours";
		yaxis="accuracy";
		gp('set xlabel "k-nearest neighbours"');
		gp('set ylabel "Accuracy"');
		gp('set xrange [1:10]');
		gp('set xtics 1.0');
		gp('set style data linespoints');
		gp('set out "output.png"');
		gp.plot(Y);
		break;


file.close();
#outputfile.close();
