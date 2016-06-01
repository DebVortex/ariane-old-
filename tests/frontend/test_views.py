import pytest

from django.core.urlresolvers import reverse


class TestLandingPageView(object):
    """Tests for the LandingPageView."""

    def test_unauthorized(self, client):
        """Test that accessing the LandingPageView unauthorized resturns 200."""
        response = client.get(reverse('index'))
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_authorized(self, login, client):
        """Test that accessing as a logged in user the LandingPageView causes an redirect."""
        response = client.get(reverse('index'))
        assert response.status_code == 302


class TestArianeView(object):
    """Tests for the ArianeView."""

    def test_unauthorized(self, client):
        """Test that accessing the LandingPageView unauthorized resturns 200."""
        response = client.get(reverse('ariane'))
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_authorized(self, login, client):
        """Test that accessing as a logged in user the LandingPageView causes an redirect."""
        response = client.get(reverse('ariane'))
        assert response.status_code == 200
