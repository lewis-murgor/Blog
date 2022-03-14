import urllib.request,json
from .models import Quote

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():

    url = base_url 

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    quote_results = []

    author = data.get('author')
    quote = data.get('quote')

    new_quote= Quote(author, quote)
    quote_results.append(new_quote)

    return quote_results