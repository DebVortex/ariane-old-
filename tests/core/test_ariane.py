import pytest


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
    def test_register(self, clean_ariane, intents, error):
        """Test that register works as expectet.

        The register function of ariane should return a AttributeError, if a keyword is already
        used or the provided language is not supported.
        """
        def test_func():
            pass
        if error:
            with pytest.raises(error):
                for intent in intents:
                    clean_ariane.register(intent, test_func)
        else:
            for intent in intents:
                clean_ariane.register(intent, test_func)
            for intent in intents:
                clean_ariane._brain[intent] == test_func
