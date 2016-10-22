from django.conf import settings

from wit import Wit


class Ariane(object):
    """Main class for Ariane, the voice controlled assitant."""

    js_files = []
    actions = {}

    def __init__(self, language):
        """Istantiate an istance of ariane.

        Args:
            language (string): a langauge string, e.g. 'en-GB'
        """
        self.language = language
        self.client = Wit(
            access_token=settings.WIT_ACCESS_TOKENS[self.language],
        )

    @classmethod
    def register(cls, intent, func):
        """Register a new function to Ariane.

        Args:
            intent (string): a string, returned by wit.ai to determine the correct function.
            func (callable): a callable that should be used, once the keyword is pressent in the
                message. Musst accept a sting as first argument.
        """
        if intent in cls.actions:
            raise AttributeError(
                "There is already a function for the intent '{}'' registerd.".format(intent)
            )
        cls.actions[intent] = func

    def handle(self, message):
        """Handle provided message and return actions for ariane frontend.

        Args:
            message (string): from SST extracted string. Used for the Wit client.
        Returns:
            dict: instructions for the ariane frontend
        """
        resp = self.client.message(message)
        # ToDo: Handle unknown or to bad confidence
        return self.actions[resp['entities']['intent'][0]['value']](self, resp)


def register(intent):
    """Register function that will be called inside the brain.py.

    Usage:
        @register("my_intent")
        def my_function(cls, message):
            [...]

    Args:
        intent (string): the intent, returned from wit.ai used to determine the correct func
    """
    def _inner_register(func):
        """Inner decorator for registering a feature.

        Args:
            func (callable): a "feature" of ariane. Musst accept a ariane instance as first
            argument and a wid response as second.
        """
        Ariane.register(intent, func)
        return func
    return _inner_register


def register_js(js_file, template_id=None):
    """Register a JS file that needs to be renderd in the frontend for the app to work.

    Args:
        js_file (string): The filepath that will be renderes in the template, using the
            {% static 'js_file' %}.

    Kwargs:
        template_id (string): The id used for the script tag in html. If provided, the type will
        be set to text/html.
    """
    Ariane.js_files.append((js_file, template_id))
