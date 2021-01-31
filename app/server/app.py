from fastapi import FastAPI

from app.server.routes.author import router as AuthorRouter
from app.server.routes.source import router as SourceRouter
from app.server.routes.article import router as ArticleRouter

app = FastAPI()

app.include_router(AuthorRouter, tags=["Author"], prefix="/author")
app.include_router(SourceRouter, tags=["Source"], prefix="/source")
app.include_router(ArticleRouter, tags=["Articles"], prefix="/article")

@app.get("/", tags=["NewsAPI"])
async def read_root():
    return {"message": "hello world"}
