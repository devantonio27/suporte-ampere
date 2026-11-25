from langchain_core.language_models.chat_models import BaseChatModel

from ampere.grafo.estado import Estado


def criar_no_gerador(modelo: BaseChatModel):
    def gerar_resposta(estado: Estado) -> dict:
        resposta = modelo.invoke(estado["mensagens"])
        return {"mensagens": [resposta]}

    return gerar_resposta
