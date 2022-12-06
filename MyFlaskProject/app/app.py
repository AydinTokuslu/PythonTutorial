from flask import Flask, render_template, request, redirect, url_for

# web sayfasına erişim, bilgileri okuma projesi
app = Flask(__name__)
# @app.route("/")
# def index():
#     return "AnaSayfa"


@app.route("/")
def index():
    numbers = [1,2,3,4,5,6,7]
    #message = "Bu bir mesajdır..."
    #return render_template("index.html", number = 10, number2 = 20)
    #return render_template("index.html", message = message)
    #return render_template("index.html", numbers = numbers)
    return render_template("index.html")

@app.route("/toplam", methods = ["GET", "POST"])
def toplam():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("number.html", total = int(number1) + int(number2))
    else:
        #return render_template("number.html")
        return redirect(url_for("index"))
#
# @app.route("/search")
# def search():
#     return "Search Page"
#
#
# @app.route("/delete/item")
# def delete():
#     return "Delete Item"
#
#
# @app.route("/delete/<string:id>")  # Dinamik URL Yapmak
# def deleteId(id):  # Dinamik URL Yapmak
#     return "Id: " + id


if __name__ == "__main__":
    app.run(debug=True)