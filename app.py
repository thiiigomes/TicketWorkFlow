from flask import Flask

from config import Config
from routes.home import home_bp
from routes.auth import auth_bp
from routes.chamados import chamados_bp

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(chamados_bp)

if __name__ == "__main__":
    app.run(debug=True)
