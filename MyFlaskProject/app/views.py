from flask import Flask, render_template

# web sayfasına erişim, bilgileri okuma projesi
app = Flask(__name__)


@app.route("/")  # decoratör
def Definition():   # herhangi bir fonksiyon ismi veriyoruz.
    #return "ilk Flask denemesi"
    return "<html><body><h1>ilk Flask denemesi</h1></body></html>"


@app.route("/hello")
def Hello():
    return render_template("hello.html")
