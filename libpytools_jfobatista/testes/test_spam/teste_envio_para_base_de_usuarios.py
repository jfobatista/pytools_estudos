from libpytools_jfobatista.spam.main import EnviadorDeSpam
from libpytools_jfobatista.testes.spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos'
    )