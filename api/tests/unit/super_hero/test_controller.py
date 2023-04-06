from unittest.mock import patch

import pytest
from fastapi import status

from super_hero.enums import HeroSuperPowerEnum


class TestSuperHeroController:
    @patch("super_hero.service.SuperHeroService.create_super_hero")
    @patch("super_hero.model.SuperHero.from_json")
    def test_create_hero(
        self,
        super_hero_model_from_json_mock,
        service_create_super_hero_mock,
        client,
        super_hero_json_data,
        super_hero_create_request_body,
        super_hero,
        hero_response_body,
    ):

        service_create_super_hero_mock.return_value = super_hero
        response = client.post("/heroes/", json=super_hero_json_data)
        service_create_super_hero_mock.assert_called_with(
            super_hero_model_from_json_mock.return_value
        )
        super_hero_model_from_json_mock.assert_called_with(super_hero_create_request_body.dict())

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == hero_response_body

    @pytest.mark.parametrize(
        "encrypt_identity, superpowers, expected_output",
        [
            (False, None, pytest.lazy_fixture("hero_response_body")),
            (True, None, pytest.lazy_fixture("encrypted_hero_response_body")),
            (False, [HeroSuperPowerEnum.FLIGHT], pytest.lazy_fixture("hero_response_body")),
            (
                True,
                [HeroSuperPowerEnum.FLIGHT],
                pytest.lazy_fixture("encrypted_hero_response_body"),
            ),
            (
                False,
                [HeroSuperPowerEnum.FLIGHT, HeroSuperPowerEnum.SPEED],
                pytest.lazy_fixture("hero_response_body"),
            ),
            (
                True,
                [HeroSuperPowerEnum.FLIGHT, HeroSuperPowerEnum.SPEED],
                pytest.lazy_fixture("encrypted_hero_response_body"),
            ),
        ],
    )
    @patch("super_hero.service.SuperHeroService.get_super_heroes")
    def test_get_heroes(
        self,
        service_get_super_heroes_mock,
        encrypt_identity,
        superpowers,
        expected_output,
        client,
        super_hero,
    ):

        service_get_super_heroes_mock.return_value = [super_hero]
        super_hero_params = (
            "&superpowers=" + "&superpowers=".join(superpowers) if superpowers else ""
        )
        print(f"/heroes?encrypt_identity={encrypt_identity}" + super_hero_params)
        response = client.get(f"/heroes?encrypt_identity={encrypt_identity}" + super_hero_params)
        service_get_super_heroes_mock.assert_called_with(superpowers)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [expected_output]
