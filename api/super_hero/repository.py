import json

from super_hero.enums import HeroSuperPowerEnum
from super_hero.model import SuperHero


class SuperHeroRepository:
    @staticmethod
    def _load_heroes():
        with open("super_hero/super_heroes.json", "r") as file_content:
            return [SuperHero(**super_hero_json) for super_hero_json in json.load(file_content)]

    _heroes = _load_heroes()

    @classmethod
    def get_all_heroes(cls):
        return cls._heroes

    @classmethod
    def get_heroes_filtered_by_superpower(cls, superpowers: list[HeroSuperPowerEnum]):
        return [
            hero
            for hero in cls._heroes
            if all(superpower in hero.superpowers for superpower in superpowers)
        ]

    @classmethod
    def save_hero(cls, hero: SuperHero):
        cls._heroes.append(hero)
        return hero
