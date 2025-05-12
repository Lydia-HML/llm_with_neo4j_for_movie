# !pip install google - generativeai
# !pip install google-ai-generativelanguage==0.6.17
# !pip install sentence-transformers
# !pip install -U langchain-huggingface
# !pip install



from graph_setup import setup_graph
from config import chat_model
from vector_setup import setup_vector_db
from qa_chain import build_graph_chain, build_vector_chain
from tools import create_tools
from agent_runner import build_agent_executor
import datetime


def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W13 Assignment 2 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

def main():

    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號

    graph = setup_graph()
    vector_db = setup_vector_db()
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    cypher_chain = build_graph_chain(graph, cypher_llm=chat_model, qa_llm=chat_model)
    vector_chain = build_vector_chain(retriever)
    tools = create_tools(vector_chain, cypher_chain)

    agent_executor = build_agent_executor(tools)

    while True:
        msg = input("我說：")
        if not msg.strip():
            break
        for chunk in agent_executor.stream({ "input": msg }):
            if 'output' in chunk:
                print(f"AI 回覆：{chunk['output']}", end="", flush=True)
        print_assignment_info(student_id)
        print()


if __name__ == "__main__":
    main()
