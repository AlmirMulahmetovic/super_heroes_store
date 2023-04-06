from utils.string import to_camel_case


def test_to_camel_case():
    assert to_camel_case("snake__case") == "snakeCase"
