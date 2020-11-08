import click
import robin_stocks as rh
import ui


login = rh.login("ajoslin87@gmail.com", "87Bluepigs!")

@click.group()
def main():
    print('hello from main')

@main.command()
@click.argument('symbols', nargs=-1)
def quote(symbols):
    quotes = rh.get_quotes(symbols)
    # print(quotes)

    for quote in quotes:
        print("{}|{}".format(quote['symbol'], quote['ask_price']))

@main.command()
def watchlist():
    print("Getting quotes for watchlist")

@main.command()
@click.argument('quantity', type=click.INT)
@click.argument('symbol', type =click.STRING)
@click.option('--limit', type=click.FLOAT)

def buy(quantity, symbol, limit):
    if limit is not None:
        ui.success("buying {} of {} at {}".format(quantity, symbol, limit))
        result = rh.order_buy_limit(symbol, quantity, limit)
    else:
        ui.sucess("buying {} of {} at {}".format(quantity,symbol))
        result = rh.order_buy_market(symbol,quantity)
@main.command()
def sell():
    pass

if __name__ =='__main__':
    main()
