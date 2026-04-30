from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Configuração do Redis vinda do ambiente
redis_host = os.getenv('REDIS_HOST', 'redis')
cache = Redis(host=redis_host, port=6379, socket_connect_timeout=2)

@app.route('/')
def home():
    try:
        # Incrementa o contador no Redis
        acessos = cache.incr('hits')
    except Exception as e:
        acessos = f"Erro de conexão com Redis ({e})"

    # Pega o nome do Pod no Kubernetes
    nome_do_pod = os.getenv('HOSTNAME', 'Local')

    return f"""
    <h1>App Full Stack</h1>
    <p><b>Quantidade de acessos:</b> {acessos}</p>
    <p><b>Rodando no Pod:</b> {nome_do_pod}</p>
    <hr>
    <p>Conectado ao Host: {redis_host}</p>
    """

if __name__ == '__main__':
    # Flask rodando na 8080 para casar com o targetPort do seu Service
    app.run(host='0.0.0.0', port=8080)