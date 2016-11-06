from ariane.apps.core import Ariane
from ariane.apps.wiki.brain import get_wiki_article


def test_get_wiki_article(
        clean_ariane, language_code, wit_access_token, wiki_response, wit_resp, mocker):
    """Test that get_wiki_article returns data in a correct way."""
    with mocker.patch('wikipedia.summary', return_value=wiki_response):
        result = get_wiki_article(Ariane(language_code), wit_resp)
        assert wiki_response == result['ariane.say']
        assert wiki_response == result['ariane.message']
