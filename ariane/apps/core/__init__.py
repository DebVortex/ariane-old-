class Ariane(object):
    """Main class for Ariane, the voice controlled assitant."""

    _brain = {}
    js_files = []

    def register(self, intent, func):
        """Register a new function to Ariane.

        Args:
            intent (string): a string, returned by wit.ai to determine the correct function.
            func (callable): a callable that should be used, once the keyword is pressent in the
                message. Musst accept a sting as first argument.
        """
        if intent in self._brain:
            raise AttributeError("Intent {} already registered.".format(intent))
        self._brain[intent] = func


def register(intent, func):
    """Register function that will be called inside the brain.py.

    Args:
        intent (string): a string, returned by wit.ai to determine the correct function.
        func (callable): a callable that should be used, once the keyword is pressent in the
            message. Musst accept a sting as first argument. Musst be able to accept a language
            kwarg.
    """
    Ariane().register(intent, func)


def register_js(js_file, template_id=None):
    """Register a JS file that needs to be renderd in the frontend for the app to work.

    Args:
        js_file (string): The filepath that will be renderes in the template, using the
            {% static 'js_file' %}.

    Kwargs:
        template_id (string): The id used for the script tag in html. If provided, the type will
        be set to text/html.
    """
    Ariane().js_files.append((js_file, template_id))
