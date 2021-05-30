#Importaciones que se realizan
import socket
import tweepy

#Hashtags que se utilizarán
hashtags=['#nomnom','#foodie','#healthylifestyle','#fresh','#madewithlove','#homemade','#chefmode','#tasty','#fruitslove','#food']
#API y Token de twitter
apikey="iHlaa81fmyMhmAo5dZ9nImRjk"
apisecret="tPH4VdTGNsdVdClU0rja8V9AZlCdEM16oWLII70rhKYaBYCY1y"
access_token="794329197657329664-Pvvjk2n4dJtQsKoKgbLkvaPLgUvJY7J"
access_token_secret="v5VtTr8rSmKvDO9ln6Z4JvvHcQmSgNKwualcU3G7qJfbD"

#Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9898))
s.listen()
conn,addr=s.accept()
print(f'conectado con {addr}')

#Funcion
class TwitterListener(tweepy.StreamListener):
    def on_status(self, status):
        diccionario=status.entities['hashtags']
        print(30*'*')
        for hashtag in diccionario:
          if '#'+str(hashtag['text']) in hashtags:
            conn.sendall(bytes(hashtag['text']+'\n',encoding='utf-8'))
            print(hashtag['text'])

#Codigo para accedes
auth=tweepy.OAuthHandler(apikey,apisecret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
streamListener = TwitterListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=hashtags)

