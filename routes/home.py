from flask import Blueprint, render_template, session, redirect, url_for

from models.usuario import listar_usuarios

from models.chamado import (
    contar_chamados,
    contar_abertos,
    contar_andamento,
    contar_fechados,
    listar_ultimos_chamados,
    contar_por_prioridade
)

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    total = contar_chamados()
    abertos = contar_abertos()
    andamento = contar_andamento()
    fechados = contar_fechados()
    prioridades = contar_por_prioridade()
    ultimos_chamados = listar_ultimos_chamados()
    
    status_chamados = {
        "Abertos": abertos,
        "Em andamento": andamento,
        "Fechados": fechados
    }

    return render_template(
    "dashboard.html",
    nome=session["nome"],
    total=total,
    abertos=abertos,
    andamento=andamento,
    fechados=fechados,
    prioridades=prioridades,
    status_chamados=status_chamados,
    ultimos_chamados=ultimos_chamados
    )


@home_bp.route("/usuarios")
def usuarios():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuarios = listar_usuarios()

    return render_template(
        "usuarios.html",
        usuarios=usuarios
    )