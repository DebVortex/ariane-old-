import pytest


@pytest.mark.django_db
def test_user_settings_update(user_settings, other_language_code):
    """Test the update function of the UserSettings model."""
    assert other_language_code != user_settings.language
    user_settings.update(language='de-DE', foo='bar')
    user_settings.refresh_from_db()
    assert other_language_code == user_settings.language
    user_settings.update()
    assert other_language_code == user_settings.language
