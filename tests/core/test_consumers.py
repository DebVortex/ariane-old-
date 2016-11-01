import json
from unittest.mock import patch

from channels import Group
from channels.tests import ChannelTestCase, apply_routes
from channels.tests.http import HttpClient
from django.contrib.auth import get_user_model

from ariane.apps.core.routing import channel_routing

user_model = get_user_model()


@apply_routes([channel_routing])
class TestWebsocketConsumer(ChannelTestCase):
    """Test the Websocket consumers."""

    def test_ws_connect_not_authenticated(self):
        """Test that ws_connect is not possible if user is not logged in."""
        client = HttpClient()
        client.send_and_consume(u'websocket.connect', {'path': "/ws"})
        response = client.receive()
        self.assertEqual(response, {"ariane.message": "Not authenticated."})

    def test_ws_connect_authenticated(self):
        """Test that ws_connect is possible if user is logged in."""
        user_model.objects.create_user('Ada Lovelace', 'user_1@test.test', '123')
        client = HttpClient()
        client.login(username='Ada Lovelace', password='123')
        client.send_and_consume(u'websocket.connect', {'path': "/ws"})
        response = client.receive()
        self.assertEqual(response, {"info": "Connected!"})

    def test_ws_message_not_authenticated(self):
        """Test that sending to ws_connect returns noting if not connected."""
        client = HttpClient()
        client.send_and_consume(u'websocket.receive', {'text': "Ping!"})
        assert not client.receive()

    @patch('django.conf.settings.WIT_ACCESS_TOKENS', {'en_GB': ''})
    @patch(
        'ariane.apps.core.Ariane.handle',
        lambda x, y: {"ariane.say": "Ping!", "ariane.message": "Ping!"}
    )
    def test_ws_message_authenticated(self):
        """Test that sending to ws_connect returns the same string."""
        user = user_model.objects.create_user('Ada Lovelace', 'user_1@test.test', '123')
        client = HttpClient()
        client.login(username=user.username, password='123')
        client.send_and_consume(u'websocket.connect', {'path': "/ws"})
        assert client.reply_channel in Group('').channel_layer._groups.get(
            'user-{}'.format(user.pk))
        client.receive()  # Drop connected message
        client.send_and_consume(u'websocket.receive',
            {'text': '{"lang": "en_GB", "message": "Ping!"}'})
        response = client.receive()
        assert response == json.loads(
            '{"ariane.say": "Ping!", "ariane.message": "Ping!"}')

    def test_ws_disconnect(self):
        """Test that disconnecting removes the reply_channel from the Group."""
        user = user_model.objects.create_user('Ada Lovelace', 'user_1@test.test', '123')
        client = HttpClient()
        client.login(username=user.username, password='123')
        client.send_and_consume(u'websocket.connect', {'path': "/ws"})
        assert client.reply_channel in Group('').channel_layer._groups.get(
            'user-{}'.format(user.pk))
        client.receive()  # Drop connected message
        client.send_and_consume(u'websocket.disconnect')
        assert not Group('').channel_layer._groups
