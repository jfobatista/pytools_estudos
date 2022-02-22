import pytest

from libpytools_jfobatista.testes.spam.enviador_de_email import Enviador, EmailInvalido

destinatarios = 'jonesjoao@gmail.com'


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['jonesjoao@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'jonesjoao_@hotmail.com',
        'Curso Python Pro',
        'Primeiro e-mail de teste'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'foobar.com.br']
)
def teste_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jonesjoao_@hotmail.com',
            'Curso Python Pro',
            'Primeiro e-mail de teste'
        )

