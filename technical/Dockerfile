FROM python:3.9

RUN pip install numpy jupyter matplotlib TA-Lib yfinance jupyterthemes

#TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr --build= $MACHTYPE --host= && \
  make && \
  make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz
