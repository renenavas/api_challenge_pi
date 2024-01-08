FROM python:3.11.5-slim
USER root
WORKDIR /app

COPY /app .

EXPOSE 8000
EXPOSE 3306

RUN pip install --upgrade pip && \
pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
