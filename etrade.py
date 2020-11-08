import pyetrade

consumer_key = "5f30ec177c4036f6c2f0c4538251cf20"
consumer_secret = "d98d22b0cd6cd464bb0a95d336ba4248"

oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
print(oauth.get_request_token())  # Use the printed URL

verifier_code = input("Enter verification code: ")
tokens = oauth.get_access_token(verifier_code)
print(tokens)
