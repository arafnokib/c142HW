from flask import Flask, jsonify, request
import csv
from storage import all_articles, liked_articles, disliked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

all_articles = []
liked_articles = []
disiked_articles = []

with open("d1_nona.csv", encoding="UTF-8") as f:
    
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

@app.route("/get-article")
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    })

@app.route("/disliked-article", methods=["POST"])
def disliked_article():
    
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status": "success"
    })
@app.route("/popular-article")
def popular_article():
    
    article_data = []
    for article in output:
        d = {
            'title' : article[12],
            'author_id' : article[5],
            'total_events' : article[15],
            'timestamp' : article[2],
            'url' : article[11],
            'lang' : article[14],
        }
        article_data.append(d)
    
    return jsonify({
        'data' : article_data,
        'status' : 'success',
    })
@app.route("/recommended-article")
def recommended_article():
    
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    
    article_data = []
    for recommended in all_recommended:
        d = {
            'title' : recommended[12],
            'author_id' : recommended[5],
            'total_events' : recommended[15],
            'timestamp' : recommended[2],
            'url' : recommended[11],
            'lang' : recommended[14],
        }
        article_data.append(d)
        
        
    
    return jsonify({
        'data' : article_data,
        'status' : 'success'
    })


if(__name__ == "__main__"):
    app.run()
    
