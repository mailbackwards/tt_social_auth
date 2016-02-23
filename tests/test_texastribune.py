import json
from social.tests.backends.oauth import OAuth2Test

from tt_social_auth import settings as tt_auth_settings


class TribOAuth2Test(OAuth2Test):
    backend_path = 'tt_social_auth.backends.texastribune.TribOAuth2'
    user_data_url = tt_auth_settings.USER_DATA_URL
    expected_username = 'foobar'
    access_token_body = json.dumps({
        'token_type': 'bearer',
        'access_token': 'foobar',
    })
    user_data_body = json.dumps({
        'username': 'foobar',
        'email': 'foo@bar.com',
        'first_name': 'Foo',
        'last_name': 'Bar'
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
