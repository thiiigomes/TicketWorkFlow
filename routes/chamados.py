from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from models.chamado import (
    listar_chamados,
    criar_chamado,
    buscar_chamado_por_id,
    atualizar_chamado,
    excluir_chamado,
    assumir_chamado,
    transferir_chamado,
    fechar_chamado
)
from models.categoria import listar_categorias
from models.prioridade import listar_prioridades
from models.equipamento import listar_equipamentos
from models.usuario import ( 
    listar_tecnicos,
    buscar_usuario_por_id
)
from models.historico import (
    registrar_historico,
    listar_historico_chamado
)

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

        chamado_id = criar_chamado(
            titulo,
            descricao,
            usuario_id,
            tecnico_id,
            categoria_id,
            prioridade_id,
            equipamento_id
        )

        registrar_historico(
            chamado_id,
            usuario_id,
            "Chamado criado",
            "O chamado foi criado com sucesso."
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

    historico = listar_historico_chamado(chamado_id)

    usuario = buscar_usuario_por_id(session["usuario_id"])

    return render_template(
        "visualizar_chamado.html",
        chamado=chamado,
        historico=historico,
        usuario=usuario
    )


@chamados_bp.route("/chamados/<int:chamado_id>/assumir", methods=["POST"])
def assumir(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuario_id = session["usuario_id"]

    # Busca o usuário logado
    usuario = buscar_usuario_por_id(usuario_id)

    # Verifica se o usuário existe
    if not usuario:

        flash(
            "Usuário não encontrado.",
            "danger"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    # Apenas técnicos podem assumir chamados
    if usuario["perfil"] not in ["Técnico", "Administrador"]:

        flash(
            "Apenas Técnicos ou Administradores podem assumir chamados.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    resultado = assumir_chamado(
        chamado_id,
        usuario_id,
        usuario_id
    )

    if resultado is False:

        flash(
            "Este chamado não pode ser assumido. "
            "Verifique se ele ainda está Aberto.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    flash(
        "Chamado assumido com sucesso!",
        "success"
    )

    return redirect(
        url_for(
            "chamados.visualizar_chamado",
            chamado_id=chamado_id
        )
    )

@chamados_bp.route(
    "/chamados/<int:chamado_id>/transferir",
    methods=["GET", "POST"]
)
def transferir(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuario_id = session["usuario_id"]

    usuario = buscar_usuario_por_id(usuario_id)

    # Apenas Técnico ou Administrador pode transferir
    if not usuario or usuario["perfil"] not in ["Técnico", "Administrador"]:

        flash(
            "Apenas Técnicos ou Administradores podem transferir chamados.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    chamado = buscar_chamado_por_id(chamado_id)

    if not chamado:

        flash(
            "Chamado não encontrado.",
            "danger"
        )

        return redirect(
            url_for("chamados.chamados")
        )

    # O chamado precisa estar em andamento
    if chamado["status"] != "Em andamento":

        flash(
            "Somente chamados Em andamento podem ser transferidos.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    if request.method == "POST":

        novo_tecnico_id = request.form["tecnico_id"]
        motivo = request.form["motivo"].strip()

        if not motivo:

            flash(
                "Informe o motivo da transferência.",
                "warning"
            )

            return redirect(
                url_for(
                    "chamados.transferir",
                    chamado_id=chamado_id
                )
            )

        resultado = transferir_chamado(
            chamado_id,
            novo_tecnico_id,
            usuario_id,
            motivo
        )

        if resultado is False:

            flash(
                "Não foi possível transferir o chamado. "
                "Verifique o técnico selecionado.",
                "warning"
            )

            return redirect(
                url_for(
                    "chamados.transferir",
                    chamado_id=chamado_id
                )
            )

        flash(
            "Chamado transferido com sucesso!",
            "success"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    tecnicos = listar_tecnicos()

    return render_template(
        "transferir_chamado.html",
        chamado=chamado,
        tecnicos=tecnicos
    )

@chamados_bp.route(
    "/chamados/<int:chamado_id>/fechar",
    methods=["GET", "POST"]
)
def fechar(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuario_id = session["usuario_id"]

    usuario = buscar_usuario_por_id(usuario_id)

    # Apenas Técnico ou Administrador pode fechar
    if not usuario or usuario["perfil"] not in ["Técnico", "Administrador"]:

        flash(
            "Apenas Técnicos ou Administradores podem fechar chamados.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    chamado = buscar_chamado_por_id(chamado_id)

    if not chamado:

        flash(
            "Chamado não encontrado.",
            "danger"
        )

        return redirect(
            url_for("chamados.chamados")
        )

    # Só pode fechar chamado Em andamento
    if chamado["status"] != "Em andamento":

        flash(
            "Somente chamados Em andamento podem ser fechados.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    # GET → abre a tela de fechamento
    if request.method == "GET":

        return render_template(
            "fechar_chamado.html",
            chamado=chamado
        )

    # POST → recebe a solução
    solucao = request.form.get("solucao", "").strip()

    if not solucao:

        flash(
            "Informe a solução do chamado antes de fechá-lo.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.fechar",
                chamado_id=chamado_id
            )
        )

    resultado = fechar_chamado(
        chamado_id,
        usuario_id,
        solucao
    )

    if resultado is False:

        flash(
            "Não foi possível fechar o chamado.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    flash(
        "Chamado fechado com sucesso!",
        "success"
    )

    return redirect(
        url_for(
            "chamados.visualizar_chamado",
            chamado_id=chamado_id
        )
    )

@chamados_bp.route("/chamados/<int:chamado_id>/editar", methods=["GET", "POST"])
def editar_chamado(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    usuario = buscar_usuario_por_id(session["usuario_id"])

    # Apenas Técnico ou Administrador pode editar chamados
    if not usuario or usuario["perfil"] not in ["Técnico", "Administrador"]:

        flash(
            "Apenas Técnicos ou Administradores podem atualizar chamados.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    chamado = buscar_chamado_por_id(chamado_id)

    if not chamado:

        flash(
            "Chamado não encontrado.",
            "danger"
        )

        return redirect(url_for("chamados.chamados"))

    # Chamados fechados não podem mais ser alterados
    if chamado["status"] == "Fechado":

        flash(
            "Este chamado está fechado e não pode mais ser alterado.",
            "warning"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        tecnico_id = request.form["tecnico_id"]
        categoria_id = request.form["categoria_id"]
        prioridade_id = request.form["prioridade_id"]
        equipamento_id = request.form["equipamento_id"]
        status = request.form["status"]

        resultado = atualizar_chamado(
            chamado_id,
            titulo,
            descricao,
            tecnico_id,
            categoria_id,
            prioridade_id,
            equipamento_id,
            status,
            session["usuario_id"]
        )

        if resultado is False:

            flash(
                "Não foi possível atualizar o chamado.",
                "warning"
            )

            return redirect(
                url_for(
                    "chamados.visualizar_chamado",
                    chamado_id=chamado_id
                )
            )

        flash(
            "Chamado atualizado com sucesso!",
            "success"
        )

        return redirect(
            url_for(
                "chamados.visualizar_chamado",
                chamado_id=chamado_id
            )
        )

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

@chamados_bp.route("/chamados/<int:chamado_id>/excluir", methods=["POST"])
def excluir_chamado_rota(chamado_id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    excluir_chamado(chamado_id)

    return redirect(url_for("chamados.chamados"))
