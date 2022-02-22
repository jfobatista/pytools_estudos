import pytest

from libpytools_jfobatista.spam.main import EnviadorDeSpam
from libpytools_jfobatista.testes.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados
