from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


movies = ["movie1", "movie2", "movie3"]

@app.route("/")
def home_page():
    # return redirect(url_for("welcome_page", name = "Goktug"))
    # return render_template("home_page.html")
    return render_template("home_page.html", id=7, movies = movies)

# @app.route("/welcome<name>")
# def welcome_page(name):
#     return "<p>Welcome {}</p>".format(name)





if __name__ == "__main__":
    app.run(debug=True)