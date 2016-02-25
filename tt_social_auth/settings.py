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

def env(var, default=None):
    result = os.environ.get(var)
    if result is None and settings is not None:
        result = getattr(settings, var, None)
    if result is None:
        result = default
    return result

# Set `TEXASTRIBUNE_BASE_URL` to the domain you're authenticating on.
# defaults to production
TEXASTRIBUNE_BASE_URL = env('TEXASTRIBUNE_BASE_URL',
    default='https://www.texastribune.org/')

# Should admins on the main Tribune site also be admins on this one?
AUTHENTICATE_TEXASTRIBUNE_STAFF = env('AUTHENTICATE_TEXASTRIBUNE_STAFF',
    default=True)

AUTHORIZATION_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'oauth2/authorize/')
ACCESS_TOKEN_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'oauth2/token/')
USER_DATA_URL = urljoin(TEXASTRIBUNE_BASE_URL, 'api/self/')
