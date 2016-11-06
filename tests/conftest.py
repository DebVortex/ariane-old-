# encoding: utf-8
import shutil
import tempfile
from functools import partial

import pytest
from faker import Faker

from ariane.apps.core import Ariane


@pytest.fixture
def loaddata(settings, db):
    """Load a Django fixture.

    Works exactly like the loaddata command. All command line options must be
    given as keyword arguments.

    There is no no need to mark the test itself with the django_db marker
    because the loaddata fixture already loads the db fixture.

    Usage::

        def test_model(loaddata):
            loaddata('my_fixture')
            # do a test using the fixture


        def test_othermodel(loaddata):
            loaddata('other_fixture', database='other')
            # do a test using the fixture
    """
    from django.core import management
    return partial(management.call_command, 'loaddata')


def pytest_runtest_setup(item):
    """Seed the Faker generator for every test.

    Faker is seeded at the beginning of each test based on the test name, so
    each test that uses Faker will use the same fake data between test runs,
    regardless of test order.

    Requires fake-factory 0.5.3 or newer.
    """
    Faker().seed(item.nodeid)


@pytest.fixture
def tmp_media_root(request, settings):
    """Create a temporary directory and use it as MEDIA_ROOT.

    The temporary directory is deleted after the test has been finished.
    """
    settings.MEDIA_ROOT = tempfile.mkdtemp()
    settings.DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    def cleanup():
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
    request.addfinalizer(cleanup)


@pytest.fixture(scope='session')
def password():
    """Return the default test password."""
    return "test"


@pytest.fixture(scope='session')
def username():
    """Return the default test username."""
    return "ada"


@pytest.fixture(scope='session')
def email():
    """Return the default test email."""
    return "ada@example.com"


@pytest.fixture
def login(client, username, email, password):
    """Return the User instance after logging the user in."""
    from django.contrib.auth import get_user_model
    user = get_user_model().objects.create_user(
        username, email="test@example.com", password=password)
    assert client.login(username=username, password=password)
    return user


@pytest.fixture
def clean_ariane():
    """Return an fresh and empty instance of ariane."""
    Ariane.actions = {}
    Ariane.js_files = []


@pytest.fixture
def wit_access_token(settings, language_code):
    """Set a fake access token for tests."""
    settings.WIT_ACCESS_TOKENS = {language_code: '1234567890'}


@pytest.fixture
def language_code():
    """Language code used for testing."""
    return 'en-GB'
