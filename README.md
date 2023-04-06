# Super heroes store

# Run the application
In order to run application (assuming that you have Docker installed on your machine) from project root folder run:
```shell
docker-compose up
```

# Run tests
In order to run tests on application running in container, enter in into container shell with:
```shell
docker exec -it super-hero-api /bin/bash
```
In docker container shell run:
```shell
pytest tests
```

# Testing
In order to test heroes get route create GET request to:
http://localhost:8000/heroes?encrypt_identity={val}&superpowers={val}&superpowers={val}
Example:
http://localhost:8000/heroes?encrypt_identity=False&superpowers=strength&superpowers=flight


In order to test heroes post route create POST request to:
http://localhost:8000/heroes/
with this(or similar) payload in raw-json format:
```json
    {
        "name": "superman",
        "identity": {
            "firstName": "clark",
            "lastName": "kent"
        },
        "birthday": "1977-04-18",
        "superpowers": ["flight", "strength", "invulnerability"]
    }
```
