from datetime import date

import pytest

from super_hero.model import SuperHero
from super_hero.schema import CreateHeroRequestBody


@pytest.fixture
def super_hero_json_data():
    return {
        "name": "superman",
        "identity": {"firstName": "clark", "lastName": "kent"},
        "birthday": "1977-04-18",
        "superpowers": ["flight", "strength", "invulnerability"],
    }


@pytest.fixture
def super_hero_create_request_body(super_hero_json_data):
    return CreateHeroRequestBody(**super_hero_json_data)


@pytest.fixture
def super_hero(super_hero_json_data):
    return SuperHero(**super_hero_json_data)


@pytest.fixture
def super_hero_with_speed():
    return SuperHero(
        name="Speed",
        identity={"firstName": "name", "lastName": "lastName"},
        birthday=date(1977, 4, 18),
        superpowers=["speed"],
    )


@pytest.fixture
def super_hero_with_speed_and_healing():
    return SuperHero(
        name="Speed",
        identity={"firstName": "name", "lastName": "lastName"},
        birthday=date(1977, 4, 18),
        superpowers=["speed", "healing"],
    )


@pytest.fixture
def super_hero_with_flight_and_strength():
    return SuperHero(
        name="FlightAndStrength",
        identity={"firstName": "name", "lastName": "lastName"},
        birthday=date(1977, 4, 18),
        superpowers=["flight", "strength"],
    )


@pytest.fixture
def super_hero_with_speed_and_flight():
    return SuperHero(
        name="SpeedAndFlight",
        identity={"firstName": "name", "lastName": "lastName"},
        birthday=date(1977, 4, 18),
        superpowers=["speed", "flight"],
    )


@pytest.fixture
def super_hero_with_strength_invulnerability_and_healing():
    return SuperHero(
        name="StrenghtInvulnerabilityAndHealing",
        identity={"firstName": "name", "lastName": "lastName"},
        birthday=date(1977, 4, 18),
        superpowers=["strength", "invulnerability"],
    )


@pytest.fixture
def hero_response_body():
    return {
        "name": "superman",
        "birthday": "1977-04-18",
        "identity": "clark kent",
        "superpowers": ["flight", "strength", "invulnerability"],
    }


@pytest.fixture
def encrypted_hero_response_body():
    return {
        "name": "superman",
        "birthday": "1977-04-18",
        "identity": "hqfwp pjsy",
        "superpowers": ["flight", "strength", "invulnerability"],
    }


@pytest.fixture
def super_heroes_with_different_superpowers(
    super_hero_with_speed,
    super_hero_with_speed_and_healing,
    super_hero_with_speed_and_flight,
    super_hero_with_flight_and_strength,
    super_hero_with_strength_invulnerability_and_healing,
):
    return [
        super_hero_with_speed,
        super_hero_with_speed_and_healing,
        super_hero_with_speed_and_flight,
        super_hero_with_flight_and_strength,
        super_hero_with_strength_invulnerability_and_healing,
    ]
