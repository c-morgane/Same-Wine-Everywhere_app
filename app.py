from flask import Flask, render_template, url_for, request
from wine_reco import get_recommandations
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

tfidf = pd.read_pickle("data/tf_idf_wine.pkl")
wine_titles = pd.read_pickle("data/wine_titles.pkl")
cosine_sim = cosine_similarity(tfidf,tfidf)

app = Flask(__name__)

@app.route("/wine_app", methods=['POST'])
def wine_app():
    recos = get_recommandations(title=request.form['wine_title'], cosine_sim=cosine_sim, titles=wine_titles)
    return render_template('appli.html', title=request.form['wine_title'], recos=recos)

@app.route("/wine_app", methods=['GET'])
def dropdown():
    return render_template('dropdown.html', wine_titles=wine_titles['title'])

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
