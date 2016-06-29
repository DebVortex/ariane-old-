from django.conf import settings


class Ariane(object):
    """Main class for Ariane, the voice controlled assitant."""

    def __init__(self):
        """Instantiate Ariane.

        This sets up the brain of Ariane. The brain is a dictionary, containing
        each supported language as key. The value, is a dictionary itself and
        will later be populated with a mapping from each supported keyword to
        the function that should be executet.
        Additionaly, this function also initializes an empty list for JS files
        that have to be rendered in the frontend.
        """
        self._brain = {lang: {} for lang in settings.ARIANE_SUPPORTED_LANGUAGES}
        self.js_files = []

    def register(self, languages, func):
        """Register a new function to Ariane.

        Args:
            languages (dict): A dictionary, containing a supported languages as key and a list of
                keywords that should be registered to the provided func.
            func (callable): a callable that should be used, once the keyword is pressent in the
                message. Musst accept a sting as first argument.
        """
        for lang in languages:
            if lang not in self._brain:
                raise AttributeError("Language {} not supported".format(lang))
            for keyword in languages[lang]:
                if keyword in self._brain[lang]:
                    raise AttributeError("Keyword {} already registered.".format(keyword))
                self._brain[lang][keyword] = func


ariane = Ariane()


def register(languages, func):
    """Register function that will be called inside the brain.py.

    Args:
        languages (dict): A dictionary, containing a supported languages as key and a list of
            keywords that should be registered to theprovided func.
        func (callable): a callable that should be used, once the keyword is pressent in the
            message. Musst accept a sting as first argument.
    """
    ariane.register(languages, func)


def register_js(js_file):
    """Register a JS file that needs to be renderd in the frontend for the app to work.

    Args:
        js_file (string): The filepath that will be renderes in the template, using the
            {% static 'js_file' %}.
    """
    ariane.js_files.append(js_file)
