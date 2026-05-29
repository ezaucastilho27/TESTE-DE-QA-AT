import pytest
from gerenciador import GerenciadorNotas

def test_calcular_media_correta():
    """Testa se o cálculo da média está correto para valores válidos."""
    gerenciador = GerenciadorNotas()
    gerenciador.cadastrar_nota(8.0)
    gerenciador.cadastrar_nota(6.0)
    assert gerenciador.calcular_media() == 7.0

def test_validar_nota_invalida_menor_que_zero():
    """Testa se o sistema rejeita notas menores que zero e gera erro."""
    gerenciador = GerenciadorNotas()
    with pytest.raises(ValueError, match="Nota inválida! A nota deve estar entre 0 e 10."):
        gerenciador.cadastrar_nota(-1.5)

def test_validar_nota_invalida_maior_que_dez():
    """Testa se o sistema rejeita notas maiores que dez e gera erro."""
    gerenciador = GerenciadorNotas()
    with pytest.raises(ValueError, match="Nota inválida! A nota deve estar entre 0 e 10."):
        gerenciador.cadastrar_nota(10.1)

def test_situacao_aprovado():
    """Testa a regra de aprovação: média >= 7."""
    gerenciador = GerenciadorNotas()
    gerenciador.cadastrar_nota(7.0)
    gerenciador.cadastrar_nota(7.5)
    assert gerenciador.verificar_situacao() == "Aprovado"

def test_situacao_recuperacao_limite_inferior():
    """Testa o limite inferior da recuperação: média exatamente 5.0."""
    gerenciador = GerenciadorNotas()
    gerenciador.cadastrar_nota(5.0)
    gerenciador.cadastrar_nota(5.0)
    assert gerenciador.verificar_situacao() == "Recuperação"

def test_situacao_recuperacao_limite_superior():
    """Testa o limite superior da recuperação: média próxima a 6.9."""
    gerenciador = GerenciadorNotas()
    gerenciador.cadastrar_nota(6.9)
    gerenciador.cadastrar_nota(6.9)
    assert gerenciador.verificar_situacao() == "Recuperação"

def test_situacao_reprovado():
    """Testa a regra de reprovação: média < 5."""
    gerenciador = GerenciadorNotas()
    gerenciador.cadastrar_nota(4.9)
    gerenciador.cadastrar_nota(4.5)
    assert gerenciador.verificar_situacao() == "Reprovado"
