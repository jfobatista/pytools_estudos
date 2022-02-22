from unittest.mock import Mock

from libpytools_jfobatista import github_api


def test_buscar_avatar():
    resposta_mock = Mock()
    resposta_mock.json.return_value = {
        'login': 'jfobatista',
        'id': 99755055,
        'node_id': 'U_kgDOBfIkLw',
        'avatar_url': 'https://avatars.githubusercontent.com/u/99755055?v=4'
    }
    github_api.requests.get = Mock(return_value=resposta_mock)
    url = github_api.buscar_avatar('jfobatista')