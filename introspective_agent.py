import os
from llama_index.agent.introspective import ToolInteractiveReflectionAgentWorker, IntrospectiveAgentWorker
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgentWorker
from llama_index.core.llms import ChatMessage, MessageRole
from database_connection import GaleriTools
from dotenv import load_dotenv

load_dotenv()

galeri_tools = GaleriTools(server=r"GORKEM", database="GaleriDB")
galeri_tool_list = galeri_tools.to_tool_list()

def get_introspective_agent(verbose=True, with_main_worker= True):

    # 1a. Critique Agent Worker tanımla.
    critique_agent_worker = FunctionCallingAgentWorker.from_tools(
        tools=galeri_tool_list,
        llm=OpenAI("gpt-3.5-turbo"),
        verbose=verbose
    )

    # 1b. Correction LLM tanımla.
    correction_llm = OpenAI("gpt-4")

    # 1c. Durdurma koşulu fonksiyonu tanımla.
    def stopping_callable(critique_str: str) -> bool:
        return "[PASS]" in critique_str

    # Introspective Agent oluşturma
    tool_interactive_reflection_agent_worker = ToolInteractiveReflectionAgentWorker.from_defaults(
        critique_agent_worker=critique_agent_worker,
        critique_template=(
            "Aşağıdaki SQL sorgusunun doğruluğunu kontrol et ve hataları düzelt.: "
            "{input_str} "
            "Veritabanı yapısına uygunluğunu ve güvenliğini değerlendir. "
            "Eğer doğruysa '[PASS]', yanlışsa '[FAIL]' yaz."
        ),
        stopping_callable=stopping_callable,
        correction_llm=correction_llm,
        verbose=verbose
    )

    # 2. Ana Agent Worker: Bu ajan, analizleri yöneten bir OpenAI modeli olarak görev yapar.
    # İsteğe bağlı olarak açılıp kapatılabilir (with_main_worker=True).
    if with_main_worker:
        main_agent_worker = OpenAIAgentWorker.from_tools(
            tools=galeri_tool_list,
            llm=OpenAI("gpt-4"),
            verbose=True
        )
    else:
        main_agent_worker = None

    introspective_agent_worker = IntrospectiveAgentWorker.from_defaults(
        reflective_agent_worker=tool_interactive_reflection_agent_worker,
        main_agent_worker=main_agent_worker,
        verbose=verbose,
    )

    # Agent'ı başlat
    chat_history = [
        ChatMessage(
            content=
            """
            Bir galeri sahibi asistanısın. Araç bilgilerini yönetmek için SQL sorgularını kullanıyorsun.
            """,
            role=MessageRole.SYSTEM,
        )
    ]

    return introspective_agent_worker.as_agent(
        chat_history=chat_history,
        verbose=verbose
    )