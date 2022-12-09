from flask import Flask, render_template, redirect, url_for, request, session, make_response
from itsdangerous import Signer, BadSignature
# web sayfasına erişim, bilgileri okuma projesi
app = Flask(__name__)
app.secret_key = b"?039eruif3__"
# b = byte cinsinden şifreyi yazıyoruz


@app.route("/")  # decoratör
def Definition():
    session['name'] = "Ahmet"
    session['username'] = "ahmet123"
    return "<html><body><h1>ilk Flask denemesi</h1></body></html>"
# @app.route("/")  # decoratör
# def Definition():   # herhangi bir fonksiyon ismi veriyoruz.
#     # cookies
#     signer = Signer("secret key")
#     signed_name = request.cookies.get("name")
#     try:
#         name = signer.unsign(signed_name).decode()
#         print('name', name)
#     except BadSignature:
#         print("bad signature")
#
#     signed_name = signer.sign("Mehmet")
#     response = make_response("<html><body><h1>ilk Flask denemesi</h1></body></html>")
#     response.set_cookie('name', signed_name)
#     #return "ilk Flask denemesi"
#     #return "<html><body><h1>ilk Flask denemesi</h1></body></html>"
#     return response


@app.route("/hello")
def Hello():
    return render_template("hello.html")

@app.route("/hello-admin")
def HelloAdmin():
    return render_template("hello_admin.html")

#https status code belirtilmemişse GET'tir, belirtilmişse POST'tur
@app.route("/hello-user/<name>")
def HelloUser(name):
    if name.lower() == "admin":
        return redirect(url_for("HelloAdmin"))
    return render_template("hello_user.html", username = name)


# @app.route("/add/<int:number1>/<int:number2>")
# def Add(number1, number2):#burda number1 number2 string, int yapmak gerekir.
#     calculation_result = number1 + number2
#     return render_template("add.html", number1 = number1, number2=number2, result=calculation_result)
# aşağıdaki farklı bir çözümü

@app.route("/add") # yazarken /add?number1=12&number2=13 olarak yazıyoruz ekrana
def Add():
    number1 = int(request.args["number1"])
    number2 = int(request.args["number2"])
    calculation_result = number1 + number2
    return render_template("add.html", number1 = number1, number2=number2, result=calculation_result)


@app.route("/login", methods=['POST','GET'])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("HelloUser", name=username))
    else:
        return render_template("login.html")

@app.route("/student")
def Student():
    return render_template("student.html")

@app.route("/result", methods=['POST'])
def Result():
    # ikinci yol - kısa olan
    ContextData = {
        "name" : request.form["name"],
        "physics" : request.form["physics"],
        "mathematics" : request.form["mathematics"],
        "chemistry" : request.form["chemistry"]
    }
    return render_template("student_result.html", **ContextData)
    # birinci yol - uzun olan
    # name = request.form["name"]
    # physics = request.form["physics"]
    # mathematics = request.form["mathematics"]
    # chemistry = request.form["chemistry"]
    # return render_template("student_result.html", name=name,
    #                        physics=physics,
    #                        mathematics=mathematics,
    #                        chemistry=chemistry)






if __name__ == "__main__":
    app.run(debug=True)