import urllib.request,json
from .models import Random_Quotes
import requests
from config import Config

base_url = None
def configure_request(app):
  global api_key,base_url
  base_url = Config.QUOTES_API
def getQuotes():
 random_quote = requests.get(base_url)
 new_quote = random_quote.json()
 id = new_quote.get("id")
 author = new_quote.get("author")
 permalink = new_quote.get("permalink")
 quote = new_quote.get("quote")
 quote_object = Random_Quotes(id,author,quote,permalink)
 return quote_object