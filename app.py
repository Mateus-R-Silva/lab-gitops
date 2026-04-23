from flask import Flask
from redis import Redis
import os


app = Flask(__name__)
redis = Redis(host='redis-s', port=6379, decode_responses=True)

@app.route('/')
def home():
    try:
        hits = redis.incr('hits')
    except Exception as e:
        hits = 'Erro de conexão com Redis'
    # Pega o nome do Pod no Kubernetes. Se não existir, usa "Local"
    nome_do_pod = os.getenv('HOSTNAME', 'Local')
    return f"""<h1>App Full Stack</h1>
    <p>Quantidade de acessos: {hits}</p>
    Rodando no Pod: {nome_do_pod}</p>"""

if __name__ == '__main__':
    # O container vai ouvir na porta 8080
    app.run(host='0.0.0.0', port=8080)