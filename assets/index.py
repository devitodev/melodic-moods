from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        album_title = request.form['album_title']
        artist = request.form['artist']
        review = request.form['review']

        # Save review to database or file
        save_review(album_title, artist, review)

        return render_template('thankyou.html')
    else:
        return render_template('index.html')

def save_review(album_title, artist, review):
    # Save review to database or file
    pass

if __name__ == '__main__':
    app.run()
