from flask import Flask, render_template      

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/index")
# def index():
#     return render_template("index.html")

@app.route("/temp")
def temp():
    return render_template("Temperature(Ambient).html")

if __name__ == "__main__":
    app.run(debug=True)