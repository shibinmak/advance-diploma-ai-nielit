import csv;
from textblob.classifiers import NaiveBayesClassifier;

train_data = [];

theFile= open("SMSSpamCollection.csv","r");
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
	tuple = data,category
	train_data.append(tuple);
print("Starting - Learning");
ourClassifier = NaiveBayesClassifier(train_data);

print(ourClassifier .classify('This restaurant is adipoli'));




