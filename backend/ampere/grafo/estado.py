from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class Estado(TypedDict):
    mensagens: Annotated[list[AnyMessage], add_messages]
