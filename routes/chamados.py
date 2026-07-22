from flask import Blueprint, render_template, session, redirect, url_for, request

from models.chamado import listar_chamados, criar_chamado
from models.categoria import listar_categorias
from models.prioridade import listar_prioridades
from models.equipamento import listar_equipamentos
from models.usuario import listar_tecnicos

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


@chamados_bp.route("/chamados/novo", methods=["GET", "POST"])
def novo_chamado():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]

        categoria_id = request.form["categoria_id"]
        prioridade_id = request.form["prioridade_id"]
        equipamento_id = request.form["equipamento_id"]
        tecnico_id = request.form["tecnico_id"]

        usuario_id = session["usuario_id"]

        criar_chamado(
            titulo,
            descricao,
            usuario_id,
            tecnico_id,
            categoria_id,
            prioridade_id,
            equipamento_id
        )

        return redirect(url_for("chamados.chamados"))

    categorias = listar_categorias()
    prioridades = listar_prioridades()
    equipamentos = listar_equipamentos()
    tecnicos = listar_tecnicos()

    return render_template(
        "novo_chamado.html",
        categorias=categorias,
        prioridades=prioridades,
        equipamentos=equipamentos,
        tecnicos=tecnicos
    )