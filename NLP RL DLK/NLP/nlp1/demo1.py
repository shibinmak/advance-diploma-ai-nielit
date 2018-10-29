from textblob import TextBlob;


someText = TextBlob("Forests house wild animals and wild life.  Forest have bees , birds, fishes and all. Mr. Salim identifies new plant species.");
print("All Words");
print(someText.words);
print("-----------");
print(someText.words[3]);
print("-----------");


theWords = someText.words;
for word in theWords:
	print (word.upper())

