from langgraph.graph import END, START, StateGraph

from ampere.grafo.estado import Estado
from ampere.grafo.nos import criar_no_gerador
from ampere.nucleo.config import Config
from ampere.nucleo.modelos import Papel, criar_modelo


def construir_grafo(config: Config):
    gerador = criar_modelo(Papel.GERADOR, config)

    grafo = StateGraph(Estado)
    grafo.add_node("gerar_resposta", criar_no_gerador(gerador))
    grafo.add_edge(START, "gerar_resposta")
    grafo.add_edge("gerar_resposta", END)
    return grafo.compile()
