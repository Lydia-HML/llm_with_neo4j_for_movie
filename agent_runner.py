from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from config import chat_model

from langchain.agents import create_tool_calling_agent


def build_agent_executor(tools):
    agent_prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位電影資料助理, 請根據上下文回答問題"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

    #agent = create_openai_tools_agent(chat_model, tools, agent_prompt) #OpenAI
    agent = create_tool_calling_agent(chat_model, tools, agent_prompt) #Google
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
