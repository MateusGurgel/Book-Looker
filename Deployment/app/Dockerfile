FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5123

RUN python setup_db.py

CMD ["sh", "-c", "cd app && streamlit run --server.port 5123 main.py"]


