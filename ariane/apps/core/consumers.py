import json

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from ariane.apps.core import Ariane


@channel_session_user_from_http
def ws_connect(message):
    """
    Consumer for ``websocket.connect``.

    If the provided user is not authenticated, a 'Not authenticated.' will be returned. Otherwise,
    he will be added to a group and the text 'Connected!' is send.

    Args:
        message (Message): message containing the reply_channel. Also used to determine if the
        user is logged in.
    """
    if message.user.is_authenticated():
        Group('user-{}'.format(message.user.pk)).add(message.reply_channel)
        Group('user-{}'.format(message.user.pk)).send({'text': '{"info": "Connected!"}'})
    else:
        message.reply_channel.send({'text': '{"ariane.message": "Not authenticated."}'})


@channel_session_user
def ws_message(message):
    """
    Consumer for ``websocket.receive``.

    If the provided user is not authenticated, nothing happens. Otherwise, the provided message
    will be returned.

    Args:
        message (Message): message containing the message to send back from the user.
    """
    if message.user.is_authenticated():
        msg = json.loads(message.content['text'])
        ariane_resp = Ariane(msg['lang']).handle(msg['message'])
        Group('user-{}'.format(message.user.pk)).send({
            "text": json.dumps(ariane_resp)
        })


@channel_session_user
def ws_disconnect(message):
    """
    Consumer for ``websocket.disconnect``.

    Removed the user from his group.

    Args:
        message (Message): message containing the user to remove from the Group.
    """
    Group('user-{}'.format(message.user.pk)).discard(message.reply_channel)
