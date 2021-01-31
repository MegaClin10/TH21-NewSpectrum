from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retrieve_article,
    retrieve_articles,
)

from app.server.models.article import (
    ErrorResponseModel,
    ResponseModel,
    ArticleSchema,
    UpdateArticleModel,
)

router = APIRouter()

#@router.get("/", response_description="Articles retrieved")
#async def get_articles():
#   articles = await retrieve_articles()
#   if articles:
#       return ResponseModel(articles, "Article data retrieved successfully")
#   return ResponseModel(articles, "Empty list returned")

@router.get("/", response_description=("Articles queried"))
async def get_articles(q: str):
    query = q
    articles = await retrieve_articles(query)
    if articles:
        return ResponseModel(articles, "Articles retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Not found in database")

@router.get("/{", response_description="Article data retrieved")
async def get_article_data(id):
    article = await retrieve_article(id)
    if article:
        return ResponseModel(article, "Source data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Source doesn't exist.")