from unittest.mock import MagicMock, patch

from super_hero.enums import HeroSuperPowerEnum
from super_hero.repository import SuperHeroRepository


class TestSuperHeroRepository:
    def test_get_all_heroes(self):
        heroes_list_mock = MagicMock()
        with patch.object(SuperHeroRepository, "_heroes", heroes_list_mock):
            assert SuperHeroRepository.get_all_heroes() == heroes_list_mock

    def test_save_heroes(self, super_hero):
        heroes_list_mock = MagicMock()
        with patch.object(SuperHeroRepository, "_heroes", heroes_list_mock):
            assert SuperHeroRepository.save_hero(super_hero) == super_hero
            heroes_list_mock.append.assert_called_with(super_hero)

    def test_get_heroes_filtered_by_superpower(
        self,
        super_hero_with_speed,
        super_hero_with_speed_and_healing,
        super_hero_with_speed_and_flight,
        super_hero_with_flight_and_strength,
        super_hero_with_strength_invulnerability_and_healing,
        super_heroes_with_different_superpowers,
    ):

        with patch.object(SuperHeroRepository, "_heroes", super_heroes_with_different_superpowers):
            result = SuperHeroRepository.get_heroes_filtered_by_superpower(
                [HeroSuperPowerEnum.SPEED, HeroSuperPowerEnum.FLIGHT]
            )
            assert super_hero_with_speed not in result
            assert super_hero_with_speed_and_healing not in result
            assert super_hero_with_speed_and_flight in result
            assert super_hero_with_flight_and_strength not in result
            assert super_hero_with_strength_invulnerability_and_healing not in result
