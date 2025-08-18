import requests

class Extract:
  def __init__(self, url):
    self.url = url

  def api_data(self):
    response = requests.get(self.url)
    return response

