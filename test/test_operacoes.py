import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores


@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)


@pytest.mark.op_simples
def test_soma_um_valor_positivo_e_um_negativo():
    v1 = 5.0
    v2 = -7.0
    assert -2 == soma(v1,v2)


@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1,v2)


@pytest.mark.op_simples
def test_sub_um_valor_positivo_e_um_negativo():
    v1 = 5.0
    v2 = -7.0
    assert 12 == sub(v1,v2)


@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1,v2)


@pytest.mark.op_simples
def test_multiplicacao_um_valor_positivo_e_um_negativo():
    v1 = 5.0
    v2 = -7.0
    assert -35 == multiplicacao(v1,v2)


@pytest.mark.op_simples
def test_divisao_dois_valores_positivos():
    v1 = 5.0
    v2 = 5.0
    assert 1 == divisao(v1,v2)


@pytest.mark.op_complexas
def test_media_de_lista_positivo():
    assert 2.5 == media_lista_valores([1,2,3,4])
