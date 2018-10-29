from textblob import TextBlob;


someText = TextBlob("Forests house wild animals and wild life.  Forest have bees , birds, fishes and all. Mr. Salim identifies new plant species.");


print("First Sentence");
print(someText.sentences[0]);


theSentences = someText.sentences;

i = 1;
print("All  Sentences");
print("----------------------");
for sentence in theSentences :
	print("Sentence " + str(i) + " : " + str(sentence));
	i = i+ 1;


