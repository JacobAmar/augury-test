FROM python:3.9-alpine3.17
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","main.py"]