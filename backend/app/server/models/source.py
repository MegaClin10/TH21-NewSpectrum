from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class SourceSchema(BaseModel):
    source: str = Field(...)
    rating: float = Field(..., gt=0, lt=200)

    class Config:
        schema_extra = {
            "example": {
                "source": "Reuters",
                "rating": 98
            }
        }

class UpdateSourceModel(BaseModel):
    source: Optional[str]
    rating: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "source": "Fox News",
                "rating": 138
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