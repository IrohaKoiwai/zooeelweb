from flask import Flask, escape, url_for, request, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog_page():
    return 'here is blog page'


@app.route('/album')
def album_page():
    return 'here is album page'


@app.route('/video')
def video_page():
    return 'here is video page'


@app.route('/labo')
def labo_page():
    return 'here is laboratory page'


@app.route('/about')
def about_page():
    return 'here is about page'


if __name__ == '__main__':
    app.run()
