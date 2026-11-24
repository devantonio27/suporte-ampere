from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

Provedor = Literal["openai", "groq"]


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql://ampere:ampere@localhost:5439/ampere"
    qdrant_url: str = "http://localhost:6333"

    modelos_falsos: bool = False
    openai_api_key: str = ""
    groq_api_key: str = ""

    provedor_gerador: Provedor = "openai"
    modelo_gerador: str = "gpt-6-luna"
    provedor_juiz: Provedor = "openai"
    modelo_juiz: str = "gpt-6.1-sol"
    provedor_trabalhador: Provedor = "groq"
    modelo_trabalhador: str = "openai/gpt-oss-120b"
