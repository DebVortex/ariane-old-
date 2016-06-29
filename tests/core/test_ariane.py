import pytest

from ariane.apps.core import Ariane


class TestAriane:
    """Test the ariane core class."""

    def test_ariane_init(self, settings):
        """Test that the class attributes are correct prepopulated.

        Note:
            * _brain must be a dict, with language codes as keys and a dict as value
            * js_files must be an empty dict
        """
        ariane = Ariane()
        for language in settings.ARIANE_SUPPORTED_LANGUAGES:
            assert language in ariane._brain
            assert ariane._brain[language] == {}
        assert ariane.js_files == []

    @pytest.mark.parametrize(
        ('extra_languages', 'error'),
        [
            [{}, None],
            [{'en-GB': ['foo', 'foo']}, AttributeError],  # Keyword already exists
            [{'zz-ZZ': ['foo']}, AttributeError],  # not supported language
        ]
    )
    def test_register(self, clean_ariane, languages, extra_languages, error):
        """Test that register works as expectet.

        The register function of ariane should return a AttributeError, if a keyword is already
        used or the provided language is not supported.
        """
        def test_func():
            pass
        if extra_languages:
            languages.update(extra_languages)
        if error:
            with pytest.raises(error):
                clean_ariane.register(languages, test_func)
        else:
            clean_ariane.register(languages, test_func)
            for lang in languages:
                for keyword in languages[lang]:
                    assert clean_ariane._brain[lang][keyword] == test_func
