from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ArticleSchema(BaseModel):
    source: dict = Field(...)
    author: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    url: str = Field(...)
    urlToImage: str = Field(...)
    publishedAt: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "source": {
                    "id": "Fox News",
                    "name": "Fox News"
                },
                "author": "John Doe",
                "title": "Dogs are the best animals! Here are 5 reasons why.",
                "description": "Informational article showing why dogs are the best pets at home...",
                "url": "https://example.com",
                "urlToImage": "https://example.com/image_uri",
                "publishedAt": "2021-01-01T00:00:00Z",
                "content": "The best animals are dogs, hands down!"
            }
        }

class UpdateArticleModel(BaseModel):
    source: Optional[dict]
    author: Optional[str]
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    urlToImage: Optional[str]
    publishedAt: Optional[str]
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "source": {
                    "id": "Fox News",
                    "name": "Fox News"
                },
                "author": "John Doe",
                "title": "Dogs are the best animals! Here are 5 reasons why.",
                "description": "Informational article showing why dogs are the best pets at home...",
                "url": "https://example.com",
                "urlToImage": "https://example.com/image_uri",
                "publishedAt": "2021-01-01T00:00:00Z",
                "content": "The best animals are dogs, hands down!"
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