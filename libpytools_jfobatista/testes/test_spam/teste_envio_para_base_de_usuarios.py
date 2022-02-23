from unittest.mock import Mock

import pytest

from libpytools_jfobatista.spam.main import EnviadorDeSpam
from libpytools_jfobatista.testes.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='João', email='jonesjoao_@ohotmail.com'),
            Usuario(nome='Francisco', email='jonesjo_@ohotmail.com')
        ],
        [
            Usuario(nome='João', email='ja@ohotmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='João', email='ja@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()  #
    enviador_de_spam = EnviadorDeSpam(sessao,
                                      enviador)  # para enviador de spam funcionar ele precisa depender de sessao e
    # de enviador, a injecao de dependencia acontece quando esses valores são fornecidos ao enviador de spam ao inves
    # de criados por ele.
    enviador_de_spam.enviar_emails(
        'ja@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    #
    enviador.enviar.assert_called_once_with(
        'ja@python.pro.br',
        'ja@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
