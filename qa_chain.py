from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_neo4j import GraphCypherQAChain
from config import chat_model



def build_graph_chain(graph, cypher_llm, qa_llm):
    return GraphCypherQAChain.from_llm(
        graph=graph,
        cypher_llm=chat_model,
        qa_llm=chat_model,
        top_k=4,
        verbose=True,
        allow_dangerous_requests=True
    )

def build_vector_chain(retriever):
    template = "請根據以下內容加上自身判斷回答問題:\n{context}\n問題: {question}"
    prompt = ChatPromptTemplate.from_template(template)
    return (
        { "context": retriever, "question": RunnablePassthrough() }
        | prompt
        | chat_model
        | StrOutputParser()
    )
