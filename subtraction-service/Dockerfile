FROM python:3.7.2-alpine3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add linux-headers build-base
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "./subtract/app.py" ]