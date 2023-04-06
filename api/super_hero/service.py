from typing import Optional

from super_hero.enums import HeroSuperPowerEnum
from super_hero.model import SuperHero
from super_hero.repository import SuperHeroRepository


class SuperHeroService:
    @staticmethod
    def create_super_hero(super_hero: SuperHero):
        return SuperHeroRepository.save_hero(super_hero)

    @staticmethod
    def get_super_heroes(superpowers: Optional[list[HeroSuperPowerEnum]] = None):
        if superpowers:
            return SuperHeroRepository.get_heroes_filtered_by_superpower(superpowers)

        return SuperHeroRepository.get_all_heroes()
