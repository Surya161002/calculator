FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir
CMD ["python","app.py"]