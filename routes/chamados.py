from flask import Blueprint, render_template, session, redirect, url_for, request

from models.chamado import (
    listar_chamados,
    criar_chamado,
    buscar_chamado_por_id,
    atualizar_chamado
)
from models.categoria import listar_categorias
from models.prioridade import listar_prioridades
from models.equipamento import listar_equipamentos
from models.usuario import listar_tecnicos

chamados_bp = Blueprint("chamados", __name__)

@chamados_bp.route("/chamados")
def chamados():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    pesquisa = request.args.get("pesquisa", "")
    status = request.args.get("status", "")
    prioridade = request.args.get("prioridade", "")
    tecnico = request.args.get("tecnico", "")

    chamados = listar_chamados(
        pesquisa,
        status,
        prioridade,
        tecnico
    )

    return render_template(
        "chamados.html",
        chamados=chamados,
        pesquisa=pesquisa,
        status=status,
        prioridade=prioridade,
        tecnico=tecnico
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

@chamados_bp.route("/chamados/<int:chamado_id>")
def visualizar_chamado(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    chamado = buscar_chamado_por_id(chamado_id)

    return render_template(
        "visualizar_chamado.html",
        chamado=chamado
    )

@chamados_bp.route("/chamados/<int:chamado_id>/editar", methods=["GET", "POST"])
def editar_chamado(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        tecnico_id = request.form["tecnico_id"]
        categoria_id = request.form["categoria_id"]
        prioridade_id = request.form["prioridade_id"]
        equipamento_id = request.form["equipamento_id"]
        status = request.form["status"]

        atualizar_chamado(
            chamado_id,
            titulo,
            descricao,
            tecnico_id,
            categoria_id,
            prioridade_id,
            equipamento_id,
            status
        )

        return redirect(url_for("chamados.visualizar_chamado", chamado_id=chamado_id))

    chamado = buscar_chamado_por_id(chamado_id)

    categorias = listar_categorias()
    prioridades = listar_prioridades()
    equipamentos = listar_equipamentos()
    tecnicos = listar_tecnicos()

    return render_template(
        "editar_chamado.html",
        chamado=chamado,
        categorias=categorias,
        prioridades=prioridades,
        equipamentos=equipamentos,
        tecnicos=tecnicos
    )