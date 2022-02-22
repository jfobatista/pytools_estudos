from unittest.mock import Mock

import pytest

from libpytools_jfobatista import github_api


@pytest.fixture
def avatar_url():
    resposta_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/99755055?v=4'
    resposta_mock.json.return_value = {
        'login': 'jfobatista',
        'id': 99755055,
        'node_id': 'U_kgDOBfIkLw',
        'avatar_url': url
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resposta_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jfobatista')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('jfobatista')
    assert url == 'https://avatars.githubusercontent.com/u/99755055?v=4'
