from sklearn.feature_extraction.text import TfidfVectorizer;
import matplotlib.pyplot as plt;
from sklearn.cluster import KMeans;
import numpy as np;
from textblob import TextBlob;
from textblob import Word;


s1 = "This is a book on birds";
s2 = "Reethu is riding a bicycle";
s3 = "Neenu is reading a book on how to ride a bicycle";
t1 = TextBlob(s1);
t2 = TextBlob(s2);
t3 = TextBlob(s3);

cntList = [];
wordIndexList = [];
wordsList = [];
tfidf = TfidfVectorizer();
dataset = [s1,s2,s3];
matrix = tfidf.fit(dataset);
#print(matrix.vocabulary_ );



dict = matrix.vocabulary_ ;
for word in dict :
#	print(word + " " +str(dict[word]));
	wordIndexList.append(dict[word]);
	cnt = t1.words.count(word) + t2.words.count(word) + t3.words.count(word);
	cntList.append(cnt);
	wordsList.append(word);

X = np.array(list(zip(wordIndexList,cntList)));

kmeans = KMeans(n_clusters=3);
kmeans.fit(X);

#print(kmeans.labels_ );


plt.scatter(wordIndexList,cntList,cmap='rainbow',c=kmeans.labels_);
plt.xticks(wordIndexList,wordsList);
plt.show();



