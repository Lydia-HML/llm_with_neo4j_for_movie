from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool

class ReviewsInput(BaseModel):
    input: str = Field(description="為使用者提出的問題")

class GraphInput(BaseModel):
    input: str = Field(description="為使用者提出的完整問題, 請保持中文語言")

def create_tools(vector_chain, graph_chain):
    reviews = StructuredTool.from_function(
        func=vector_chain.invoke,
        name="Reviews",
        description="這是一個關於電影評論的向量資料庫",
        args_schema=ReviewsInput
    )
    graph = StructuredTool.from_function(
        func=graph_chain.invoke,
        name="Graph",
        description="這是一個包含演員、導演與電影風格的圖形資料庫",
        args_schema=GraphInput
    )
    return [reviews, graph]
