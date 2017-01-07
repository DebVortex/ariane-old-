import pytest

from django.core.urlresolvers import reverse

from ariane.apps.users.models import UserSetting


@pytest.mark.django_db
def test_update_user_settings_view_get(login, client):
    """Test get of the user_setting view.

    If the user does not have a UserSetting object, it should be created.
    """
    assert UserSetting.objects.filter(user=login).count() == 0
    url = reverse('user_settings')
    response = client.get(url)
    assert response.status_code == 200
    assert UserSetting.objects.filter(user=login).count() == 1


@pytest.mark.django_db
def test_update_user_settings_view_post(login, client, user_settings, other_language_code):
    """Test post of the user_setting view.

    The language has to be changed after the successful call.
    """
    assert user_settings.user == login
    assert other_language_code != user_settings.language
    url = reverse('user_settings')
    response = client.post(url, data={'language': other_language_code})
    assert response.status_code == 200
    user_settings.refresh_from_db()
    assert other_language_code == user_settings.language
