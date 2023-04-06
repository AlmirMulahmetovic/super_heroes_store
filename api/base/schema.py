from pydantic import BaseModel

from utils.string import to_camel_case


class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        orm_mode = True
