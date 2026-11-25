import pytest
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from ampere.nucleo.config import Config
from ampere.nucleo.falsos import ModeloFalso
from ampere.nucleo.modelos import Papel, criar_modelo


def config(**kwargs) -> Config:
    base = dict(openai_api_key="chave-de-teste", groq_api_key="chave-de-teste")
    return Config(_env_file=None, **(base | kwargs))


@pytest.mark.parametrize("papel", list(Papel))
def test_modelos_falsos_respondem_sem_rede(papel):
    modelo = criar_modelo(papel, config(modelos_falsos=True))
    assert isinstance(modelo, ModeloFalso)
    resposta = modelo.invoke("oi")
    assert papel.value in resposta.content


def test_provedor_padrao_do_gerador_e_openai():
    assert isinstance(criar_modelo(Papel.GERADOR, config()), ChatOpenAI)


def test_trabalhador_usa_groq_por_padrao():
    assert isinstance(criar_modelo(Papel.TRABALHADOR, config()), ChatGroq)


def test_trocar_provedor_nao_exige_mudar_codigo():
    cfg = config(provedor_gerador="groq", modelo_gerador="openai/gpt-oss-20b")
    assert isinstance(criar_modelo(Papel.GERADOR, cfg), ChatGroq)


def test_config_le_variaveis_de_ambiente(monkeypatch):
    monkeypatch.setenv("MODELO_GERADOR", "modelo-x")
    assert Config(_env_file=None).modelo_gerador == "modelo-x"


@pytest.mark.integration
def test_gerador_real_responde():
    cfg = Config()
    if not cfg.openai_api_key:
        pytest.skip("sem OPENAI_API_KEY no .env")
    resposta = criar_modelo(Papel.GERADOR, cfg).invoke("Diga oi em 3 palavras")
    assert resposta.content
