import pytest

from ariane.apps.core import Ariane


@pytest.fixture
def language_code():
    """Language code used for testing."""
    return 'en-GB'


@pytest.fixture
def wit_access_token(settings, language_code):
    settings.WIT_ACCESS_TOKENS = {language_code: '1234567890'}


@pytest.fixture
def clean_ariane():
    """Return an fresh and empty instance of ariane."""
    Ariane.actions = {}
    Ariane.js_files = []


@pytest.fixture
def jsfile_path():
    """Example filepath used for register_js."""
    return 'foo/bar.js'
