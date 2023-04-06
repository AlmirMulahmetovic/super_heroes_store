from enum import Enum


class HeroSuperPowerEnum(str, Enum):
    STRENGTH = "strength"
    SPEED = "speed"
    FLIGHT = "flight"
    INVULNERABILITY = "invulnerability"
    HEALING = "healing"
