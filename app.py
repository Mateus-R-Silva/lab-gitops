from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def home():
    hits = redis.incr('hits')
    # Pega o nome do Pod no Kubernetes. Se não existir, usa "Local"
    nome_do_pod = os.getenv('HOSTNAME', 'Local')
    return f"""
    <h1>Sistema de Contagem de Visitas</h1>
    <p>Esta página foi vista {hits} vezes.</p>
    <p>Respondido no Pod: {nome_do_pod}</p>"
    """
    
if __name__ == '__main__':
    # O container vai ouvir na porta 8080
    app.run(host='0.0.0.0', port=8080)