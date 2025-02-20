from flask import Flask, request, render_template

app = Flask(__name__)

# Sample dictionary of Bible verses by topic
bible_verses = {
    "faith": ["Hebrews 11:1 - Now faith is the assurance of things hoped for, the conviction of things not seen.",
              "Romans 10:17 - So faith comes from hearing, and hearing through the word of Christ."],
    "love": ["1 Corinthians 13:4-5 - Love is patient, love is kind. It does not envy, it does not boast, it is not proud.",
             "John 3:16 - For God so loved the world that he gave his one and only Son."],
    "strength": ["Philippians 4:13 - I can do all things through Christ who strengthens me.",
                 "Isaiah 40:31 - But those who hope in the Lord will renew their strength."]
}

@app.route("/", methods=["GET", "POST"])
def home():
    verse_list = []
    if request.method == "POST":
        topic = request.form["topic"].lower()
        verse_list = bible_verses.get(topic, ["No verses found for this topic."])
    return render_template("index.html", verses=verse_list)

if __name__ == "__main__":
    app.run(debug=True)
