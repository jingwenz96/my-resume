from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    courses = [
    'MISY330',
    'MISY350',
    'ECON301'
    ]

    return render_template('courses.html', courses=courses)


if __name__ == '__main__':
    app.run(debug=True)
