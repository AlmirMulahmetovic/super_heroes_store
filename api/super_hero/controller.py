from typing import Union

from fastapi import APIRouter, Body, Query, status

from super_hero.enums import HeroSuperPowerEnum
from super_hero.model import SuperHero
from super_hero.schema import (
    CreateHeroRequestBody,
    EncryptedHeroResponseBody,
    HeroResponseBody,
)
from super_hero.service import SuperHeroService

heroes_router = APIRouter(prefix="/heroes")


@heroes_router.post("", status_code=status.HTTP_201_CREATED, response_model=HeroResponseBody)
def create_hero(herro_body: CreateHeroRequestBody = Body()):
    return SuperHeroService.create_super_hero(SuperHero.from_json(herro_body.dict()))


@heroes_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Union[list[HeroResponseBody], list[EncryptedHeroResponseBody]],
)
def get_heroes(
    encrypt_identity: bool = Query(False), superpowers: list[HeroSuperPowerEnum] = Query(None)
):
    return [
        HeroResponseBody.from_orm(hero)
        if not encrypt_identity
        else EncryptedHeroResponseBody.from_orm(hero)
        for hero in SuperHeroService.get_super_heroes(superpowers)
    ]
