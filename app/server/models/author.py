from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class AuthorSchema(BaseModel):
    fullname: str = Field(...)
    rating: float = Field(..., gt=0, lt=200)
    consr_votes: int = Field(..., gt=0)
    libr_votes: int = Field(..., gt=0)
    neutr_votes: int = Field(..., gt = 0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "rating": 78,
                "consr_votes": 25,
                "libr_votes": 106,
                "neutr_votes": 47
            }
        }

class UpdateAuthorModel(BaseModel):
    fullname: Optional[str]
    rating: Optional[float]
    consr_votes: Optional[int]
    libr_votes: Optional[int]
    neutr_votes: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "rating": 156,
                "consr_votes": 26,
                "libr_votes": 105,
                "neutr_votes": 47
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}