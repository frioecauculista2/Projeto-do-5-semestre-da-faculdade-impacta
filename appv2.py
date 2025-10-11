from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "segredo"

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="joaosiqueira08!",
        database="avaliacoes_db"
    )

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

@app.route("/login", methods=["GET", "POST"])
def login():
    # Se já estiver logado, vai para o painel
    if "usuario_id" in session:
        return redirect("/painel")

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, nome FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
        usuario = cur.fetchone()
        conn.close()

        if usuario:
            session["usuario_id"] = usuario[0]
            session["usuario_nome"] = usuario[1]
            return redirect("/painel")
        else:
            return "<h1>Usuário ou senha inválidos</h1>"

    return render_template("login.html")

@app.route("/painel")
def painel():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template("painel.html")

@app.route("/logout")
def logout():
    session.clear()  # limpa todos os dados da sessão
    return redirect("/login")  # volta para a tela de login

if __name__ == "__main__":
    app.run(debug=True)