from decouple import config, Csv
client_id = config("CLIENT_ID")
client_secret = config("CLIENT_SECRET")
# redirect_uri = config("REDIRECT_URI" )
REDIRECT_URI = "http://127.0.0.1:8000/spotify/redirect"
 
