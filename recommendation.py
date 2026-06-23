import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("products.csv")

tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(df['Description'])

similarity = cosine_similarity(tfidf_matrix)

def recommend(product_name):

    index = df[df['Product'] == product_name].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in scores[1:4]:
        recommendations.append(
            df.iloc[i[0]]['Product']
        )

    return recommendations