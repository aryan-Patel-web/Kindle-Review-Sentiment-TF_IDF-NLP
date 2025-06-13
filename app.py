from flask import Flask, render_template, request
import pickle

# Load vectorizer and model
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)
with open('nb_model_tfidf.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    # ...existing code...
    if request.method == 'POST':
        review = request.form['review']
        review_transformed = tfidf.transform([review]).toarray()  # Convert to dense
        pred = model.predict(review_transformed)[0]
        prediction = 'Positive' if pred == 1 else 'Negative'
# ...existing code...
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)