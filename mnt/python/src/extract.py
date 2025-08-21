import requests

class ExtractAPi:
    """Coleta os dados da API e retorna um JSON."""
    def __init__(self, url):
        self.url = url

    def extract(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            if response.text:  # Verifica se a resposta não está vazia
                content_type = response.headers.get('Content-Type')
                if 'application/json' in content_type:
                    return response.json()
                else:
                    raise Exception(f"Formato de resposta inesperado: {content_type}")
            else:
                raise Exception("A resposta está vazia.")
        else:
            raise Exception(f"Erro na requisição: {response.status_code} - {response.text}")

