import pytest

from ariane.apps.core import Ariane


@pytest.fixture
def clean_ariane(settings):
    """Return an fresh and empty instance of ariane."""
    ariane = Ariane()
    ariane._brain = {}
    ariane.js_files = []
    return ariane


@pytest.fixture
def jsfile_path():
    """Example filepath used for register_js."""
    return 'foo/bar.js'
