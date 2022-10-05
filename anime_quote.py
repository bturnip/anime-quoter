'''
# --------------------------------------------------------------------
# anime_quote.py
# 20221005 Danny Anderson <bturnip@Heyday>
# --------------------------------------------------------------------
'''
import json
import requests

SELF_TEST=False

API_URL= 'https://animechan.vercel.app/api/random'

def get_anime_quote():
    '''
    Uses animechan api to return a random anime quote.
    Returns a json dict with the following keys
    ['anime', 'character', 'quote']
    '''
    api_req= requests.get(API_URL, timeout=15)
    quote = json.loads(api_req.text)
    return quote

if(SELF_TEST):
    new_quote = get_anime_quote()
    print(f'+++DEBUG: new_quote: {new_quote}')
    print(f'+++DEBUG: data type: {type(new_quote)}')
    print(f'+++DEBUG: dict keys: {new_quote.keys()}')
