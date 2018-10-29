from sklearn.feature_extraction.text import TfidfVectorizer;
from sklearn.metrics.pairwise import cosine_similarity;


s1 = "The study of bees , birds, butterflies and animals is Zoology";
s2 = "Enneagram is the study of the divrse set of human minds";
s3 = "Botony is the study of the plants kingdom";

q = "Botony is the study of the plants kingdom . It a rich collection";

data_set = [s1,s2,s3];
tfidf = TfidfVectorizer();

matrix = tfidf.fit(data_set);

data_set = [q,s1,s2,s3];

matrix = tfidf.fit_transform(data_set);
print("Similarity ");
print("-----------------");
print(cosine_similarity(matrix[0:1], matrix));
print("-----------------");
