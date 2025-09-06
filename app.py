from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def about_me():
    return render_template('aboutme.html', titlename='About Me')

# @app.route("/lifestyle")
# def lifestyle():
#     return render_template('lifestyle.html', titlename='Lifestyle')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5500)