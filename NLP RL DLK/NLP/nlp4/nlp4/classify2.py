import csv;
theFile= open("SMSSpamCollection1.csv","r");
csvreader = csv.reader(theFile,delimiter=",");

for line in csvreader:
	
	theline = str(line);
	theline = theline.replace("[","");
	theline = theline.replace("]","");
	theline = theline.replace("'","");
	theline = theline.replace("\"","");
	parts = theline.split(",");
	category = parts[0];
#	category = category.trim();
	data = parts[1]
	print(data);
	print(category);




