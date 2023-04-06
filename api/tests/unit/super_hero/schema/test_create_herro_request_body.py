import pytest

from super_hero.enums import HeroSuperPowerEnum
from super_hero.schema import CreateHeroRequestBody


class TestCreateHeroRequestBody:
    def test_superpowers_validation_valid_values(self):
        assert CreateHeroRequestBody.must_be_valid_superpower(
            [
                HeroSuperPowerEnum.FLIGHT,
                HeroSuperPowerEnum.HEALING,
            ]
        ) == [HeroSuperPowerEnum.FLIGHT, HeroSuperPowerEnum.HEALING]

    def test_superpowers_validation_invalid_values(self):
        with pytest.raises(ValueError, match="InvalidSuperpower is not valid super power."):
            CreateHeroRequestBody.must_be_valid_superpower(
                [HeroSuperPowerEnum.FLIGHT, HeroSuperPowerEnum.HEALING, "InvalidSuperpower"]
            )
