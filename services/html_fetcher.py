import requests
from bs4 import BeautifulSoup

class HTMLFetcher:
    def __init__(self, timeout=10):
        self.timeout = timeout
    
    def fetch(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            return BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            return None
