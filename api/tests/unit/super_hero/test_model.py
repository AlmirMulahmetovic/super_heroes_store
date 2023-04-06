from super_hero.model import SuperHero, SuperHeroIdentity


class TestSuperHero:
    def test_super_hero_from_json(self, super_hero_json_data):
        hero = SuperHero.from_json(super_hero_json_data)

        assert isinstance(hero, SuperHero)
        assert hero.name == super_hero_json_data.get("name")
        assert hero.birthday == super_hero_json_data.get("birthday")
        assert hero.identity.first_name == super_hero_json_data.get("identity").get("firstName")
        assert hero.identity.last_name == super_hero_json_data.get("identity").get("lastName")
        assert hero.superpowers == super_hero_json_data.get("superpowers")

    def test_super_hero_identity_from_json(self, super_hero_json_data):
        super_hero_identity = SuperHeroIdentity.from_json(super_hero_json_data.get("identity"))

        assert isinstance(super_hero_identity, SuperHeroIdentity)
        assert super_hero_identity.first_name == super_hero_json_data.get("identity").get(
            "firstName"
        )
        assert super_hero_identity.last_name == super_hero_json_data.get("identity").get("lastName")
