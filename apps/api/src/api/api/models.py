from pydantic import BaseModel

class RagRequest(BaseModel):
    query: str

class RAGResponse(BaseModel):
    answer: str