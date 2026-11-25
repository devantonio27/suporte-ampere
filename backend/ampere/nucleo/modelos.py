from enum import StrEnum

from langchain_core.language_models.chat_models import BaseChatModel

from ampere.nucleo.config import Config
from ampere.nucleo.falsos import ModeloFalso


class Papel(StrEnum):
    GERADOR = "gerador"
    JUIZ = "juiz"
    TRABALHADOR = "trabalhador"


def _openai(modelo: str, config: Config) -> BaseChatModel:
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(model=modelo, api_key=config.openai_api_key)


def _groq(modelo: str, config: Config) -> BaseChatModel:
    from langchain_groq import ChatGroq

    return ChatGroq(model=modelo, api_key=config.groq_api_key)


def _gemini(modelo: str, config: Config) -> BaseChatModel:
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(model=modelo, google_api_key=config.google_api_key)


PROVEDORES = {"openai": _openai, "groq": _groq, "gemini": _gemini}


def criar_modelo(papel: Papel, config: Config) -> BaseChatModel:
    if config.modelos_falsos:
        return ModeloFalso(papel=papel.value)

    provedor = getattr(config, f"provedor_{papel.value}")
    modelo = getattr(config, f"modelo_{papel.value}")
    return PROVEDORES[provedor](modelo, config)
