def get_recommandations(title, cosine_sim, titles):
    idx = titles[titles==title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    wine_indices = [i[0] for i in sim_scores]
    return titles.iloc[wine_indices]
