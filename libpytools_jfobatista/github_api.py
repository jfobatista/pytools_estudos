import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuárioo no gitHub
    :param usuario: str com o nome de usuário no github
    :return: str com link do avatar do usuário.
    """
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('jfobatista'))
