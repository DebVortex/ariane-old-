import pytest

from ariane.apps.core import ariane


@pytest.fixture
def clean_ariane(settings):
    """Return an fresh and empty instance of ariane."""
    ariane._brain = {key: {} for key in settings.ARIANE_SUPPORTED_LANGUAGES}
    ariane.js_files = []
    return ariane


@pytest.fixture
def languages(settings):
    """Return languages and keywords used for register."""
    lngs = {key: ['foo', 'bar'] for key in settings.ARIANE_SUPPORTED_LANGUAGES}
    return lngs


@pytest.fixture
def jsfile_path():
    """Example filepath used for register_js."""
    return 'foo/bar.js'
