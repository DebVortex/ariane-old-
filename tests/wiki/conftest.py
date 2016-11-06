import pytest


@pytest.fixture
def wiki_response():
    return "Lorem Ipsum dolor sit amet..."


@pytest.fixture
def wit_resp(wiki_response):
    return {'entities': {'wikipedia_search_query': [{'value': wiki_response}]}}
