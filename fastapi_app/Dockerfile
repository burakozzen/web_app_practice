FROM python:3.10

RUN pwd

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app/

COPY . /app

WORKDIR /app

EXPOSE 8888

CMD ["uvicorn","fastapi_app.main:app","--host","0.0.0.0","--port","8888"]