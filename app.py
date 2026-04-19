from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home()
    # Pega o nome do Pod no Kubernetes. Se não existir, usa "Local"
    nome_do_pod = os.getenv('HOSTNAME', 'Local')
    return f"<h1>App do Mateus v1.0</h1><p>Rodando no Pod: {nome_do_pod}</p>"

if __name__ == '__main__':
    # O container vai ouvir na porta 8080
    app.run(host='0.0.0.0', port=8080)