FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

ENV FLASK_APP=barista.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
