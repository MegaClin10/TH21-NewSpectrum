from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class AuthorSchema(BaseModel):
    fullname: str = Field(...)
    rating: float = Field(..., gt=0, lt=200)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "rating": 78
            }
        }

class UpdateAuthorModel(BaseModel):
    fullname: Optional[str]
    rating: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "rating": 156
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