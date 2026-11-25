from langchain_core.messages import AIMessage, HumanMessage

from ampere.grafo.montagem import construir_grafo
from ampere.nucleo.config import Config


def grafo_falso():
    return construir_grafo(Config(_env_file=None, modelos_falsos=True))


def test_grafo_responde_a_uma_mensagem():
    resultado = grafo_falso().invoke({"mensagens": [HumanMessage("Qual o prazo de entrega?")]})
    assert isinstance(resultado["mensagens"][-1], AIMessage)


def test_historico_e_acrescentado_nao_substituido():
    resultado = grafo_falso().invoke({"mensagens": [HumanMessage("oi")]})
    assert len(resultado["mensagens"]) == 2  # a pergunta + a resposta


def test_grafo_tem_o_no_esperado():
    assert "gerar_resposta" in set(grafo_falso().get_graph().nodes)
