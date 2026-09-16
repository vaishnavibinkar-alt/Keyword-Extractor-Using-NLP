import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")

def extract_keywords(text, top_n=10):
    stop_words = stopwords.words("english")

    vectorizer = TfidfVectorizer(stop_words=stop_words)

    tfidf_matrix = vectorizer.fit_transform([text])

    scores = tfidf_matrix.toarray()[0]
    words = vectorizer.get_feature_names_out()

    keyword_scores = list(zip(words, scores))

    keyword_scores.sort(key=lambda x: x[1], reverse=True)

    return [word for word, score in keyword_scores[:top_n]]