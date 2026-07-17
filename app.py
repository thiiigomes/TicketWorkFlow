from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Ticket Workflow</h1><p>Sistema iniciado com sucesso!</p>"

if __name__ == "__main__":
    app.run(debug=True)
