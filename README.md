# Projeto IaC - Meu App Python

Este projeto contém a Infraestrutura como Código (IaC) para o deploy de uma aplicação web simples em Python usando Kubernetes.

## 🏗️ Arquitetura

O manifesto `app-iac.yaml` declara dois recursos principais no cluster Kubernetes:

1. **Deployment (`meu-app-python`)**:
   - Garante a execução de **2 réplicas** (Pods) para alta disponibilidade.
   - Utiliza a imagem Docker oficial enxuta `python:3.9-slim`.
   - Ao iniciar, cria dinamicamente um arquivo `index.html` com a mensagem *"Olá do cluster do Mateus!"* e levanta um servidor web nativo do Python na porta `8080`.

2. **Service (`meu-app-service`)**:
   - Cria um serviço interno do tipo **ClusterIP**.
   - Escuta o tráfego na porta `80` e faz o balanceamento de carga redirecionando as requisições para a porta `8080` dos pods da aplicação.

## 🚀 Como executar

Certifique-se de que você tem acesso a um cluster Kubernetes rodando (via Minikube, Kind, ou nuvem) e o `kubectl` devidamente configurado.

Aplique as configurações executando o seguinte comando na raiz do diretório:

```bash
kubectl apply -f app-iac.yaml
```

## 🧪 Como testar

Como o Service foi criado como `ClusterIP`, a aplicação só é acessível internamente pelo cluster. Para acessá-la e testá-la através de seu navegador local, execute um `port-forward`:

```bash
kubectl port-forward svc/meu-app-service 8080:80
```

Em seguida, abra o seu navegador e acesse:
http://localhost:8080

## ⚙️ Integração Contínua (CI)

O projeto conta com uma pipeline de Integração Contínua (CI) configurada via **GitHub Actions** (`.github/workflows/ci.yml`). 

Sempre que um novo código é enviado (`push`) para o repositório, um fluxo automatizado é acionado para:
- Configurar um ambiente de testes em uma máquina Linux rodando Python 3.9.
- Instalar o `flake8` (ferramenta de verificação de estilo e sintaxe).
- Validar o código Python (como o arquivo `app.py`) em busca de erros de sintaxe ou digitação, garantindo a qualidade do código antes de qualquer implantação.