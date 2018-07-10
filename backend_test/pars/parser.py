import bs4, requests
from .models import UrlModel, H1_tag

def parse_url(url):
    url.h1_tags.all().delete()

    req = requests.get(url.url)
    b = bs4.BeautifulSoup(req.text, 'html.parser')
    url.charset = req.encoding
    url.title = b.findAll('title')
    for tag in b.findAll('h1'):
        h1 = H1_tag()
        h1.url = url
        h1.tag = str(tag)
        h1.save()
    url.success = True

    return (url)