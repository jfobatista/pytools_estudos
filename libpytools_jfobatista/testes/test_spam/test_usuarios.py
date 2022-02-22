from libpytools_jfobatista.testes.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='João')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='João'), Usuario(nome='Francisco')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
