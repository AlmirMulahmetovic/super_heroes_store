from glob import glob

import pytest
from fastapi.testclient import TestClient

from app import app

# ingest all fixtures into pytest plugins
pytest_plugins = [
    fixture.replace("/", ".").replace("\\", ".").replace(".py", "")
    for fixture in glob("tests/fixtures/**/*.py", recursive=True)
    + glob("tests/integration/fixtures/**/*.py", recursive=True)
    if "__" not in fixture
]


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
