#!pip install langchain langchain_openai rich
#!pip install neo4j langchain_community
#!pip install -U langchain-neo4j

import os
from rich import print as pprint
from langchain_openai import ChatOpenAI
import openai
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv(override=True)



# 匯入套件和金鑰

#預設匯入時就會從 OPENAI_API_KEY 環境變數讀取金鑰
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f'\nOPENAI_API_KEY={openai.api_key} \nOPENAI_API_KEY is ready!')
#建立 OpenAI 物件
llm = init_chat_model("gpt-3.5-turbo", model_provider="openai")
response = llm.invoke("Hello, Langchain world!")
print(response)
print("\nLangchain Framework for OpenAI is ready,too :-) ")


from langchain_neo4j import GraphCypherQAChain, Neo4jGraph

# Get environment secrets
# Load secrets from environment variables
NEO4J_URI = os.getenv('NEO4J_URI')  # Use default localhost if not set
NEO4J_USERNAME=os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')  # Replace with a default if needed
# Logging the Neo4j URL being used
print(f"Attempting connection to Neo4j at: {NEO4J_URI}")


# from neo4j import GraphDatabase
# # URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
# URI = "neo4j+ssc://27447525.databases.neo4j.io:7687"
# AUTH = ("neo4j", NEO4J_PASSWORD)
# with GraphDatabase.driver(URI, auth=AUTH) as driver:
#     driver.verify_connectivity()

# Initialize the Neo4j graph object
try:
    # Initialize the Neo4jGraph object
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,  # Standard default username; replace if required
        password=NEO4J_PASSWORD,
    )
    print("Successfully connected to Neo4j database.")
except ValueError as e:
    print(f"Error while connecting to the Neo4j database: {e}")
    raise

# Initialize Chain
cypher_chain = GraphCypherQAChain.from_llm(
    graph=graph,
    llm=llm,
    top_k=4,
    verbose=True,
    allow_dangerous_requests=True
)

print("Successfully initialized CypherQAChain.")
