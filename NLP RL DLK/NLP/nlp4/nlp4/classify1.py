from textblob.classifiers import NaiveBayesClassifier;

train_data = [('This is a good book','pos'),('This is a nice article','pos'),('this film is interesting','pos'),('This book is boring','neg'),('This place in nasty','neg'),('This place has rude people','neg'),('This is adipoli','pos')];

ourClassifier = NaiveBayesClassifier(train_data);

print(ourClassifier .classify('This restaurant is adipoli'));


