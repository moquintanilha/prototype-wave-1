import json
from fastapi import APIRouter
from app.src.models.people import People

router = APIRouter(
    tags=['Create People'],
    responses={500: {"description": "Internal server error"}},
)


@router.post(
        '/create',
        response_model=People
        )
async def create_people(people: People):
    try:
        req = {
            'name': people.name,
            'birth_date': people.birth_date,
            'country': people.country
        }
        return req
    except Exception as e:
        raise e
