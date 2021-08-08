from flask import Flask, jsonify, request
import csv
allArticle = []
with open(r'C:\Users\vedan\Desktop\Flask API\article.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticle = data[1:]
likedArticle = []
notLikedArticle = []
didNotWatch = []
app = Flask(__name__)

@app.route("/get_article")
def get_movies():
    return jsonify({
        "data": allArticle[0],
        "status": "success"
    })
@app.route("/liked_article",methods = ["POST"])
def liked_movies():
    movie = allArticle[0]
    liked_movies.append(movie)
    allArticle.pop(0)
    return jsonify({
        "status": "success"
    })
@app.route("/unliked_article", method = ["POST"])
def unliked_movies():
    movie = allArticle[0]
    unliked_movies.appen(movie)
    allArticle.pop(0)
    return jsonify({
        "status": "success"
    })
if __name__ == "__main__":
    app.run()