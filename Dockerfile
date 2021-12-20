FROM python:3.9

WORKDIR /app

COPY . /app

RUN tar -xf ta-lib-0.4.0-src.tar.gz

WORKDIR /app/ta-lib

RUN ./configure --prefix=/usr --build=aarch64-unknown-linux-gnu x86_64-unknown-linux-gnu


RUN make

RUN make install

WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# CMD ["mqtt_app.py"]

ENTRYPOINT ["python3"]
