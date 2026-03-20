FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
COPY servidor_central.py servidor_central.py
RUN pip install -r requirements.txt
# Exponemos el puerto del cerebro
EXPOSE 9090
CMD ["python", "servidor_central.py"]