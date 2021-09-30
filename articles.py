from flask import Flask, jsonify, Request
import csv
all_articles=[]
with open('articles.csv',encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
liked_articles=[]
disliked_articles=[]

app=Flask(__name__)
@app.route("/all-articles",methods=["GET"])
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"succes"
    })
@app.route("/liked-articles",methods=["POST"])
def lliked_articles():
    article=all_articles[0]
    l_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"succes"
    }),201
@app.route("/disliked-articles",methods=["POST"])
def unliked_articles():
    article=all_articles[0]
    d_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status":"succes"
    }),201
if __name__=="__main__":
    app.run()
