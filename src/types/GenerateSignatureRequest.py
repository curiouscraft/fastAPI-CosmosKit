# models.py

from pydantic import BaseModel

class GenerateSignatureRequest(BaseModel):
    data: dict