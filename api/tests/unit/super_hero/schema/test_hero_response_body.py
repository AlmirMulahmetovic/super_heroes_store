from super_hero.schema import HeroResponseBody


class TestHeroResponseBody:
    def test_from_orm(self, super_hero):
        result = HeroResponseBody.from_orm(super_hero)

        assert isinstance(result, HeroResponseBody)
        assert result.name == super_hero.name
        assert str(result.birthday) == str(super_hero.birthday)
        assert result.identity == super_hero.full_name
        assert result.superpowers == super_hero.superpowers
