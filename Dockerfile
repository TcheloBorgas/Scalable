# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create log directory and set proper permissions
RUN mkdir -p /usr/src/app/logs && chown -R nobody:nogroup /usr/src/app/logs

# Copy the application directory contents into the container at /usr/src/app
COPY ./app /usr/src/app

# Copy supervisord configuration file and other necessary files
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ["Template Scalable Test - Página1.csv", "temp_file.csv", "./"]

# Expose the ports used by Flask and Streamlit
EXPOSE 5000 8501

# Set the command to run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
