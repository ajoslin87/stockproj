FROM python:3.9

WORKDIR /app

COPY . /app

RUN tar -xf ta-lib-0.4.0-src.tar.gz

WORKDIR /app/ta-lib

RUN ./configure --prefix=/usr --build= $MACHTYPE --host= $HOST

RUN make

RUN make install

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "mqtt_app.py"]

# ENTRYPOINT ["python3"]

