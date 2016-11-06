import pytest

from ariane.apps.core import Ariane


@pytest.fixture
def wit_response():
    """Example response from the wit client."""
    return {'entities': {'intent': [{'value': 'test_intent'}]}}


@pytest.fixture
def ariane_with_intent(clean_ariane):
    """Create an Ariane instance with an example intent and action."""
    def test_func(ariane, msg):
        return 'Success!'
    Ariane.register('test_intent', test_func)


@pytest.fixture
def jsfile_path():
    """Example filepath used for register_js."""
    return 'foo/bar.js'
