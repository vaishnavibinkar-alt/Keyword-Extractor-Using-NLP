from flask import Flask, render_template, request
from keyword_extractor import extract_keywords

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    keywords = []
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        if text.strip():
            keywords = extract_keywords(text)

    return render_template(
        "index.html",
        keywords=keywords,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)