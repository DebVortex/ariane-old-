import pytest


@pytest.fixture
def wiki_response():
    """Example responsetext for the wikipedia package."""
    return "Lorem Ipsum dolor sit amet..."


@pytest.fixture
def wit_resp(wiki_response):
    """WitResponse to pass into get_wiki_article."""
    return {'entities': {'wikipedia_search_query': [{'value': wiki_response}]}}
