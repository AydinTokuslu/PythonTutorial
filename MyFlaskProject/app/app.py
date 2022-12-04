from flask import Flask, render_template

# web sayfasına erişim, bilgileri okuma projesi
app = Flask(__name__)
@app.route("/")
def index():
    return "AnaSayfa"


@app.route("/search")
def search():
    return "Search Page"


@app.route("/delete/item")
def delete():
    return "Delete Item"


@app.route("/delete/<string:id>")  # Dinamik URL Yapmak
def deleteId(id):  # Dinamik URL Yapmak
    return "Id: " + id


if __name__ == "__main__":
    app.run(debug=True)