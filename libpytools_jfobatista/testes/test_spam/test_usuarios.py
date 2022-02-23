from libpytools_jfobatista.testes.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='João', email='jonesjoao_@ohotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='João', email='jonesjoao_@ohotmail.com'), Usuario(nome='Francisco', email='jonesjoao_'
                                                                                                       '@ohotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
