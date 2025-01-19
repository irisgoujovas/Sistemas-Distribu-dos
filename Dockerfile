# Imagem base
FROM python:3.10

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos para o container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta
EXPOSE 5003

# Comando para iniciar o serviço
CMD ["python", "app.py"]
