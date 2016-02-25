from social.backends.oauth import BaseOAuth2

from .. import settings as tt_auth_settings


class TribOAuth2(BaseOAuth2):
    """Texas Tribune OAuth authentication backend"""
    name = 'texastribune'
    AUTHORIZATION_URL = tt_auth_settings.AUTHORIZATION_URL
    ACCESS_TOKEN_URL = tt_auth_settings.ACCESS_TOKEN_URL
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'email'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('expires_in', 'expires_in')
    ]

    def get_user_details(self, response):
        """Return user details from Texas Tribune account"""
        return {
            'username': response.get('username'),
            'email': response.get('email') or '',
            'first_name': response.get('first_name') or '',
            'last_name': response.get('last_name') or '',
            # Only authenticate staff
            'is_staff': (response.get('is_staff', False) and
                         tt_auth_settings.AUTHENTICATE_TEXASTRIBUNE_STAFF)
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json(
            tt_auth_settings.USER_DATA_URL,
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )
