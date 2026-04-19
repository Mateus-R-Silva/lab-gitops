# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala o Flask lá dentro
RUN pip install flask

# Copia o seu app.py para dentro do container
COPY app.py .

# Comando para iniciar a aplicação
CMD ["python", "app.py"]