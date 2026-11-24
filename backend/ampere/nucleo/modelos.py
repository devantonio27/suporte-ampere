from enum import StrEnum

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from ampere.nucleo.config import Config
from ampere.nucleo.falsos import ModeloFalso


class Papel(StrEnum):
    GERADOR = "gerador"
    JUIZ = "juiz"
    TRABALHADOR = "trabalhador"


def criar_modelo(papel: Papel, config: Config) -> BaseChatModel:
    if config.modelos_falsos:
        return ModeloFalso(papel=papel)

    provedor = getattr(config, f"provedor_{papel.value}")
    modelo = getattr(config, f"modelo_{papel.value}")

    if provedor == "openai":
        return ChatOpenAI(model=modelo, api_key=config.openai_api_key)
    return ChatGroq(model=modelo, api_key=config.groq_api_key)
