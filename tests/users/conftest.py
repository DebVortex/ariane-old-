import pytest

from ariane.apps.users import models


@pytest.fixture
def user_settings(login):
    """Create and return UserSetting for the as login used User."""
    setting, _ = models.UserSetting.objects.get_or_create(user=login)
    return setting
