from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_article,
    retrieve_articles,
)

from server.models.article import (
    ErrorResponseModel,
    ResponseModel,
    ArticleSchema,
    UpdateArticleModel,
)

router = APIRouter()

@router.get("/", response_description="Articles retrieved")
async def get_articles():
    articles = await retrieve_articles()
    if articles:
        return ResponseModel(articles, "Article data retrieved successfully")
    return ResponseModel(articles, "Empty list returned")

@router.get("/{id}", response_description="Article data retrieved")
async def get_article_data(id):
    article = await retrieve_article(id)
    if article:
        return ResponseModel(article, "Source data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Source doesn't exist.")