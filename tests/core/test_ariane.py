from unittest.mock import patch

import pytest

from ariane.apps.core import Ariane


class TestAriane:
    """Test the ariane core class."""

    @pytest.mark.parametrize(
        ('intents', 'error'),
        [
            [[], None],
            [['intent1'], None],
            [['intent1', 'intent2'], None],
            [['intent1', 'intent1'], AttributeError],  # intent already exists
        ]
    )
    def test_register(
            self, clean_ariane, wit_access_token, language_code, intents, error):
        """Test that register works as expectet.

        The register function of ariane should return a AttributeError, if a keyword is already
        used or the provided language is not supported.
        """
        def test_func():
            pass

        if error:
            with pytest.raises(error):
                for intent in intents:
                    Ariane.register(intent, test_func)
        else:
            for intent in intents:
                Ariane.register(intent, test_func)
            ariane = Ariane(language_code)
            for intent in intents:
                ariane.actions[intent] == test_func

    def test_handle(self, ariane_with_intent, wit_access_token, wit_response, language_code):
        """Test that handle is able to take care of a Wit response."""
        with patch('wit.Wit.message', lambda x, y: wit_response):
            ariane = Ariane(language_code)
            assert ariane.handle('') == 'Success!'
