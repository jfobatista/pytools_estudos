import requests

#está efetivamente acessando a api do git.
def buscar_avatar(usuario):
    """
    Busca o avatar de um usuárioo no gitHub
    :param usuario: str com o nome de usuário no github
    :return: str com link do avatar do usuário.
    """
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


