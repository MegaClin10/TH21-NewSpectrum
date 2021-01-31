from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_source,
    delete_source,
    retrieve_source,
    retrieve_sources,
    update_source,
)

from app.server.models.source import (
    ErrorResponseModel,
    ResponseModel,
    SourceSchema,
    UpdateSourceModel,
)

router = APIRouter()

@router.post("/", response_description="Source data added into the database")
async def add_source_data(author: SourceSchema = Body(...)):
    source = jsonable_encoder(source)
    new_source = await add_source(source)
    return ResponseModel(new_source, "Source added successfully.")

@router.get("/", response_description="Sources retrieved")
async def get_sources():
    sources = await retrieve_sources()
    if sources:
        return ResponseModel(sources, "Sources data retrieved successfully")
    return ResponseModel(sources, "Empty list returned")

@router.get("/{id}", response_description="Source data retrieved")
async def get_source_data(id):
    source = await retrieve_source(id)
    if source:
        return ResponseModel(source, "Source data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Source doesn't exist.")

@router.put("/{id}")
async def update_source_data(id: str, req: UpdateSourceModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_source = await update_source(id, req)
    if updated_source:
        return ResponseModel(
            "Source with ID: {} name update is successful".format(id),
            "Source name updated successfully",
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "There was an error updating the source.",
    )

@router.delete("/{id}", response_description="Source data deleted from the database")
async def delete_source_data(id: str):
    deleted_source = await delete_source(id)
    if deleted_source:
        return ResponseModel(
            "Source with ID: {} removed".format(id), "Source deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Source with id {0} doesn't exist".format(id)
    )