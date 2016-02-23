import os
try:
    from django.conf import settings
except ImportError:
    # Not django
    settings = None
try:
    from urlparse import urljoin
except ImportError:
    # python 3
    from urllib.parse import urljoin

_default_base_url = 'https://www.texastribune.org/'
if settings is None:
    TEXASTRIBUNE_BASE_URL = os.environ.get('TEXASTRIBUNE_BASE_URL', _default_base_url)
else:
    TEXASTRIBUNE_BASE_URL = getattr(settings, 'TEXASTRIBUNE_BASE_URL', _default_base_url)

AUTHORIZATION_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'oauth2/authorize/')
ACCESS_TOKEN_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'oauth2/token/')
USER_DATA_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'api/self/')
