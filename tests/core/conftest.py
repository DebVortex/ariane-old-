import pytest


@pytest.fixture
def message_factory():
    class FakeReplyChannel:
        messages = []
        name = "test"

        def send(self, message):
            self.messages.append(message)

    class FakeMessage(dict):
        def __init__(self, path=None, method=None, reply_channel=None, content=None,
                http_session=None):
            self.http_session = self.session = http_session
            self.content = content if content else {}
            self.reply_channel = reply_channel if reply_channel else FakeReplyChannel()
            self['path'] = path if path else '/'
            self['method'] = method if method else 'FAKE'
    return FakeMessage
