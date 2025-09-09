from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "segredo"

##CONEXÃO AO MYSQL
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="joaosiqueira08!",
        database="avaliacoes_db"
    )

##ETAPA DE CADASTRO DO USUÁRIO
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)