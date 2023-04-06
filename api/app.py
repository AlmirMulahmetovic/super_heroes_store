from fastapi import FastAPI

from super_hero.controller import heroes_router

app = FastAPI()
app.include_router(heroes_router)
