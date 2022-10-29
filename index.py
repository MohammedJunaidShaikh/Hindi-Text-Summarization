from flask import Flask, render_template, url_for, request
from summarize import summarize

app = Flask(__name__)


@app.route('/')
# @app.route('/home')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    name1 = summarize(name)
    print(name1)
    return render_template('summary.html', name=name1)


if __name__ == "__main__":
    # app.run(debug=False, host='0.0.0.0')
    # app.run(debug=True)
    app.run(debug=True, use_reloader=True)
