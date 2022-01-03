import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

d1 = pd.read_csv("d1_nona.csv")



count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(d1['soup'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)
d1 = d1.reset_index()
indices = pd.Series(d1.index, index = d1['contentId'])

def get_recommendations(contentId, cosine_sim):
  idx = indices[contentId]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  article_indices = [i[0] for i in sim_scores]
  return d1['contentId'].iloc[article_indices]

