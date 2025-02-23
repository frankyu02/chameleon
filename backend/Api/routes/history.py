﻿from fastapi import APIRouter, Depends
from Api.service.history_service import HistoryService
from typing import Annotated
from Api.dependencies import get_history_service, get_user
from Api.repository.user_authentication_repository import User

router = APIRouter(
    # specify sub-route. All routes in this file will be in the form of /login/{whatever}
    prefix="/history",
    # tags are strictly for metadata (helps with openAPI specifications)
    tags=["history"],
    # also metadata
    responses={401: {"description": "Incorrect Login information"}},
)

@router.get("/")
async def get_user_history(
    history_service: Annotated["HistoryService", Depends(get_history_service)],
    user: Annotated['User', Depends(get_user)]
):
    return await history_service.get_history(user)
