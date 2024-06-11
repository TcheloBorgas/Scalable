# Use uma imagem base leve do Python
FROM python:3.11-slim

# Instale dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application directory contents into the container at /usr/src/app
COPY ./app /usr/src/app

# Explicitly copy the template directory
COPY ./app/template /usr/src/app/template

# Copy supervisord configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy other necessary files
COPY ["Template Scalable Test - Página1.csv", "temp_file.csv", "./"]

# Expose the ports used by Flask and Streamlit
EXPOSE 5000 8501

# Set the command to run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

