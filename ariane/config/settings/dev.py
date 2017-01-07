import socket
import subprocess

from configurations import values

from . import common, databases


class Development(databases.Databases, common.Common):
    """Settings for development."""

    CACHES = values. DictValue({
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    })

    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')

    # devserver must be ahead of django.contrib.staticfiles
    INSTALLED_APPS = common.Common.INSTALLED_APPS + ('debug_toolbar',)

    MIDDLEWARE_CLASSES = common.Common.MIDDLEWARE_CLASSES + [
        'debug_toolbar.middleware.DebugToolbarMiddleware']

    @property
    def MIDDLEWARE_CLASSES(self):
        """Return a tuple of middleware classes, as strings.

        While using the Development class, DebugToolbarMiddleware has to be
        added to the MIDDLEWARE_CLASSES to work propper.
        """
        return super().MIDDLEWARE_CLASSES + (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

    @property
    def INTERNAL_IPS(self):
        """Return a tuple of IP addresses, as strings.

        Detect a Vagrant box by looking at the hostname. Return the gateway IP
        address on a Vagrant box, because this is the IP address the request
        will originate from.
        """
        if 'vagrant' in socket.gethostname():
            addr = [line.split()[1] for line in subprocess.check_output(['netstat', '-rn']).splitlines() if line.startswith('0.0.0.0')][0]  # noqa
        else:
            addr = '127.0.0.1'
        return (addr,)
