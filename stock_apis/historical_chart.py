from yahoo_fin import stock_info as si
from yahoo_fin import get_quote_table as qt

def historical_chart(ticker):

    historical = si.get_data(ticker,start_date = starting_date, end_date = ending_date)
    df = pd.DataFrame(historical)
    df.index.name = 'date'
    json_data=df.to_json(orient='split')
    print(df)
    print(json_data)
    # mqttc.publish("aj/switch/historical", json_data)

def simpler_call(ticker):
    print(ticker)
    
    ticker_price = si.get_live_price(ticker)

    mqttc.publish("aj/switch/ticker_price", ticker_price)