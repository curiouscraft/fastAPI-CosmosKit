# services.py

from fastapi import Query
from pydantic import BaseModel
from src.types.GenerateSignatureRequest import GenerateSignatureRequest
# from types.GenerateSignatureRequest import GenerateSignatureRequest

# class GenerateSignatureRequest(BaseModel):
#     data: dict

class SignatureService:

    async def getGenerateSignature(self, skip: int = Query(0, description="Number of items to skip"), 
                                          limit: int = Query(10, description="Maximum number of items to return")):
        return {"skip": skip, "limit": limit}

    async def postGenerateSignature(self, request_body: GenerateSignatureRequest):
        print(request_body.dict(), 'request_body')
        return {"status": "skip", "limit": "s"}

signatureService = SignatureService()  # Create an instance of SignatureService
