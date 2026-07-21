from flask import Blueprint, render_template, session, redirect, url_for

from models.usuario import listar_usuarios

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))
    
    return render_template(
        "dashboard.html",
        nome=session["nome"]
    )