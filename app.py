from flask import Flask, render_template, request
import pickle
import numpy as np
from difflib import SequenceMatcher


with open("popular.pkl",'rb') as file:
    popular_books = pickle.load(file)
    
with open('pt.pkl','rb') as file:
    pt = pickle.load(file)
    
with open('books.pkl','rb') as file:
    books = pickle.load(file)

with open('similarity_scores.pkl','rb') as file:
    similarity_score = pickle.load(file)

    
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_recommendations(book_name):
    if book_name not in pt.index:
        best_match = max(pt.index, key=lambda x: similar(book_name, x))
        print(f"Book name not found. Using most similar book: {best_match}")
        book_name = best_match

    index = np.where(pt.index == book_name)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []

    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    
    recommendations = []
    for i in data:
        temp = {"book": i[0], "author": i[1], "image": i[2]}
        recommendations.append(temp)
    return recommendations
    


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_name = request.form["book_name"]
        recommendations = get_recommendations(book_name)
        return render_template("index.html", recommendations=recommendations)
    return render_template("index.html", recommendations=None)

if __name__ == "__main__":
    app.run(debug=True)
