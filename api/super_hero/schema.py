from datetime import date

from pydantic import validator

from base.schema import BaseSchema
from deesee_encryption.service import DeeSeeEncryptionService
from super_hero.enums import HeroSuperPowerEnum
from super_hero.model import SuperHero


class HeroIdentity(BaseSchema):
    first_name: str
    last_name: str


class CreateHeroRequestBody(BaseSchema):
    name: str
    identity: HeroIdentity
    birthday: date
    superpowers: list[str]

    @validator("superpowers")
    def must_be_valid_superpower(cls, v: list[str]):
        valid_superpowers = [value for value in HeroSuperPowerEnum]
        for power in v:
            if power not in valid_superpowers:
                raise ValueError(f"{power} is not valid super power.")

        return v


class HeroResponseBody(BaseSchema):
    name: str
    birthday: date
    identity: str
    superpowers: list[str]

    @classmethod
    def from_orm(cls, orm_obj: SuperHero):
        return cls(
            name=orm_obj.name,
            birthday=orm_obj.birthday,
            identity=orm_obj.full_name,
            superpowers=orm_obj.superpowers,
        )


class EncryptedHeroResponseBody(HeroResponseBody):
    @validator("identity")
    def encrypt_identity(cls, v: str):
        return DeeSeeEncryptionService.encrypt_string(v)
