from langchain_community.vectorstores import Neo4jVector
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import OPENAI_API_KEY, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

import requests, os


def setup_vector_db():
    output_dir = "dataset"
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    url = 'https://FlagTech.github.io/F4763/movie_reviews.csv'

    with open('movie.csv', 'wb') as f:
        f.write(requests.get(url).content)

    loader = CSVLoader('./movie.csv')
    docs = loader.load()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small",
                                  api_key=OPENAI_API_KEY)

    # 需先刪掉 vector，才能再建新的 embeddings
    #   CALL db.index.fulltext.drop('vector')
    #embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    #embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small") #微軟

    db = Neo4jVector.from_documents(
        docs,
        embedding=embeddings,
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
    return db
