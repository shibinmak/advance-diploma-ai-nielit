from textblob import TextBlob;


someText = TextBlob("Forests house wild animals and wild life.  Forest have bees , birds, fishes and all. Mr. Salim identifies new plant species.");


print(someText.translate(to="es"));

