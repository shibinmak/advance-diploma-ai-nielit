from sklearn.feature_extraction.text import TfidfVectorizer;



s1 = "The study of bees , birds, butterflies and animals is Zoology";
s2 = "Enneagram is the study of the divrse set of human minds";
s3 = "Botony is the study of the plants kingdom";

q = "about plants";

data_set = [s1,s2,s3];
tfidf = TfidfVectorizer();

matrix = tfidf.fit(data_set);
#print(matrix);

dict = matrix.vocabulary_;
print("Items List " + str(dict.items()));
print("--------------------------------");
print("Dict Keys " + str(dict.keys()));


data_set = [q,s1,s2,s3];
matrix = tfidf.fit_transform(data_set);
