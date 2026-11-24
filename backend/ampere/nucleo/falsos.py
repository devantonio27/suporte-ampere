from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class ModeloFalso(BaseChatModel):
    papel: str

    @property
    def _llm_type(self) -> str:
        return "falso"

    def _generate(self, messages, stop=None, run_manager=None, **kwargs) -> ChatResult:
        ultima = messages[-1].content if messages else ""
        texto = f"[falso:{self.papel}] {ultima}"
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=texto))])
