from flask import Blueprint, render_template, session, redirect, url_for

from models.notificacao import (
    listar_notificacoes,
    contar_notificacoes_nao_lidas,
    marcar_notificacao_como_lida
)


notificacoes_bp = Blueprint(
    "notificacoes",
    __name__
)


@notificacoes_bp.route("/notificacoes")
def notificacoes():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuario_id = session["usuario_id"]

    notificacoes = listar_notificacoes(usuario_id)

    total_nao_lidas = contar_notificacoes_nao_lidas(
        usuario_id
    )

    return render_template(
        "notificacoes.html",
        notificacoes=notificacoes,
        total_nao_lidas=total_nao_lidas
    )

@notificacoes_bp.route(
    "/notificacoes/<int:notificacao_id>/ler",
    methods=["POST"]
)
def marcar_como_lida(notificacao_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    marcar_notificacao_como_lida(
        notificacao_id,
        session["usuario_id"]
    )

    return redirect(
        url_for("notificacoes.notificacoes")
    )