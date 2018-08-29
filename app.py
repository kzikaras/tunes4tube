from flask import Flask, Response, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rock')
def rock_page():
    rock_songs = [
        {'name': 'song1'},
        {'name': 'song2'},
        {'name': 'song3'}
        ]
    return render_template('rock.html', songs=rock_songs)

@app.route('/electronic')
def electronic_page():
    electronic_songs = []
    return render_template('electronic.html', songs=electronic_songs)

@app.route('/other')
def other_page():
    other_songs = []
    return render_template('other.html', songs=other_songs)

    

if __name__ == "__main__":
    app.run(debug=True)
