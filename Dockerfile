# Use uma imagem base leve do Python
FROM python:3.11-slim

# Instale dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie a configuração do supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Crie os diretórios de log
RUN mkdir -p /var/log/supervisor

# Copie os arquivos da aplicação para o diretório de trabalho
COPY app/ .

# Exponha as portas que serão usadas pelo Streamlit e Flask
EXPOSE 8501
EXPOSE 5000

# Comando para iniciar o supervisord, que gerencia ambos os processos
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
