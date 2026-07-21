from flask import Blueprint, render_template, session, redirect, url_for
from models.chamado import listar_chamados

chamados_bp = Blueprint("chamados", __name__)

@chamados_bp.route("/chamados")
def chamados():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    chamados = listar_chamados()

    return render_template(
        "chamados.html",
        chamados=chamados
    )