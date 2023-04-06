from unittest.mock import patch

import pytest

from super_hero.enums import HeroSuperPowerEnum
from super_hero.service import SuperHeroService


class TestSuperHeroService:
    @patch("super_hero.repository.SuperHeroRepository.save_hero")
    def test_create_super_hero(self, repository_save_hero_mock, super_hero):
        assert (
            SuperHeroService.create_super_hero(super_hero) == repository_save_hero_mock.return_value
        )
        repository_save_hero_mock.assert_called_with(super_hero)

    @pytest.mark.parametrize(
        "superpowers", [None, [HeroSuperPowerEnum.HEALING, HeroSuperPowerEnum.SPEED]]
    )
    @patch("super_hero.repository.SuperHeroRepository.get_heroes_filtered_by_superpower")
    @patch("super_hero.repository.SuperHeroRepository.get_all_heroes")
    def test_get_super_heroes(
        self,
        repository_get_all_heroes_mock,
        repository_get_heroes_filtered_by_superpower_mock,
        superpowers,
    ):
        heroes = SuperHeroService.get_super_heroes(superpowers)
        (
            repository_get_all_heroes_mock.assert_not_called()
            if superpowers
            else repository_get_all_heroes_mock.assert_called()
        )
        repository_get_heroes_filtered_by_superpower_mock.assert_called_with(
            superpowers
        ) if superpowers else repository_get_heroes_filtered_by_superpower_mock.assert_not_called()

        assert heroes == (
            repository_get_heroes_filtered_by_superpower_mock.return_value
            if superpowers
            else repository_get_all_heroes_mock.return_value
        )
