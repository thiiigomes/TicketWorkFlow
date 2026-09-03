from flask import Flask, session

from config import Config

from routes.home import home_bp
from routes.auth import auth_bp
from routes.chamados import chamados_bp
from routes.notificacoes import notificacoes_bp
from models.notificacao import contar_notificacoes_nao_lidas

app = Flask(__name__)

app.config.from_object(Config)

@app.context_processor
def notificacoes_globais():

    if "usuario_id" not in session:
        return {
            "total_notificacoes_nao_lidas": 0
        }

    total = contar_notificacoes_nao_lidas(
        session["usuario_id"]
    )

    return {
        "total_notificacoes_nao_lidas": total
    }

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(chamados_bp)
app.register_blueprint(notificacoes_bp)

if __name__ == "__main__":
    app.run(debug=True)
