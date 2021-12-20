def simpler_call(ticker)
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S")
            
    ticker_price = si.get_live_price(ticker)

    d = {"date": timestamp, "price": ticker_price}

    df = pd.DataFrame(data=d, index = [0])

    mqttc.publish("aj/switch/tsla", ticker_price)


