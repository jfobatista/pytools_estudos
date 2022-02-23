# Arquivo que disponibiliza as fixtures Conexão e Sessão para outros módulos
import pytest

from libpytools_jfobatista.testes.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()
