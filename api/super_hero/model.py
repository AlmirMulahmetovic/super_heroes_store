from datetime import date

from super_hero.enums import HeroSuperPowerEnum


class SuperHeroIdentity:
    def __init__(self, first_name=None, last_name=None):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @classmethod
    def from_json(cls, data: dict[str, str]):
        return cls(
            data.get("first_name") or data.get("firstName"),
            data.get("last_name") or data.get("lastName"),
        )

    def __repr__(self) -> str:
        return f"first_name: {self._first_name}, last_name: {self._last_name}"


class SuperHero:
    def __init__(
        self,
        name: str,
        identity: dict[str, str],
        birthday: date,
        superpowers: list[HeroSuperPowerEnum],
    ):
        self._name = name
        self._identity = SuperHeroIdentity.from_json(identity)
        self._birthday = birthday
        self._superpowers = superpowers

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def identity(self) -> SuperHeroIdentity:
        return self._identity

    @identity.setter
    def identity(self, value: SuperHeroIdentity):
        self._identity = value

    @property
    def birthday(self) -> date:
        return self._birthday

    @birthday.setter
    def birthday(self, value: date):
        self._birthday = value

    @property
    def superpowers(self) -> list[HeroSuperPowerEnum]:
        return self._superpowers

    @superpowers.setter
    def superpowers(self, value: list[HeroSuperPowerEnum]):
        self._superpowers = value

    @property
    def full_name(self):
        return f"{self._identity.first_name} {self._identity.last_name}"

    @classmethod
    def from_json(cls, data: dict[str, str]):
        return cls(
            data.get("name"), data.get("identity"), data.get("birthday"), data.get("superpowers")  # type: ignore  # noqa: E501
        )

    def __repr__(self) -> str:
        return f"name: {self._name}, identity: [{self._identity}], birthday: {self._birthday}, superpowers: {self._superpowers}"  # noqa: E501
