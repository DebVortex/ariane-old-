from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    if message.user.is_authenticated():
        Group(message.user.username).add(message.reply_channel)
        Group(message.user.username).send({'text': 'Conected!'})
    else:
        message.reply_channel.send({'text': 'Not authenticated.'})


@channel_session_user
def ws_message(message):
    if message.user.is_authenticated():
        Group(message.user.username).send({
            "text": "[{name}}] {message}".format(
                user=message.user.username,
                message=message.content['text'],
            )
        })


@channel_session_user
def ws_disconnect(message):
    Group(message.user.username).discard(message.reply_channel)
