# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala o Flask 
RUN pip install flask

RUN pip install redis
# Copia o app.py para dentro do container
COPY app.py .

# Comando para iniciar a aplicação
CMD ["python", "app.py"]