from flask import Blueprint, render_template, request, redirect, url_for, session

from models.usuario import buscar_usuario_por_email

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if "usuario_id" in session:
        return redirect(url_for("home.home"))

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        usuario = buscar_usuario_por_email(email)

        if usuario and usuario["senha"] == senha:

            session["usuario_id"] = usuario["id"]
            session["nome"] = usuario["nome"]
            session["perfil"] = usuario["perfil"]

            return redirect(url_for("home.home"))

        return render_template(
            "login.html",
            erro="E-mail ou senha inválidos."
        )

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))
