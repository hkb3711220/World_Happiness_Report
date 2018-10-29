import requests
from bs4 import BeautifulSoup

class GET_URL(object):

    def __init__(self):
        self.HEADER = {'User-Agent': 'Mozilla/5.0'}

    def response(self, url):
        try:
            response = requests.get(url, headers = self.HEADER)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

        soup = BeautifulSoup(response.text, 'lxml')

        return soup
