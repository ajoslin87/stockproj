import pyetrade

consumer_key = "5f30ec177c4036f6c2f0c4538251cf20"
consumer_secret = "d98d22b0cd6cd464bb0a95d336ba4248"
tokens = {'oauth_token': 'RZbnr7mGTsPB5d8vpwmwzyz9IWxhupk2AS9pC4ch2w8=',
          'oauth_token_secret': 'KwV6yG13+faCFFkQdv3Otoa02qWN+VnSZHu9kPFLwRY='}

accounts = pyetrade.ETradeAccounts(
    consumer_key,
    consumer_secret,
    tokens['oauth_token'],
    tokens['oauth_token_secret']
)

# print(accounts.list_accounts())

# print(accounts.get_account_balance('vQMsebA1H5WltUfDkJP48g'))

# print(accounts.get_account_balance('dBZOKt9xDrtRSAOl4MSiiA'))

print(accounts.get_account_balance('6_Dpy0rmuQ9cu9IbTfvF2A'))
