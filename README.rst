tt\_social\_auth
----------------

This package is a custom `python-social-auth`_ backend for the Texas Tribune.

.. _python-social-auth: https://github.com/omab/python-social-auth

Drop it into your app of choice to get TT OAuth2 working (relatively) quickly.

Installation: Django
--------------------

The majority of this is the same as installing ``python-social-auth`` directly.
If you run into problems or confusions, `consult their docs`_.

.. _consult their docs: https://python-social-auth.readthedocs.org

- Register your app in the main Texas Tribune project. Talk to Tech if you need help with this. This will give you a client ID and secret key.
- Add ``tt_social_auth`` to ``requirements.txt``
- Add ``social.apps.django_app.default`` to ``INSTALLED_APPS``
- Add ``tt_social_auth.backends.texastribune.TribOAuth2`` to ``AUTHENTICATION_BACKENDS`` (*NOTE:* you want to keep Django's default auth backend too; see `Django docs`_ for details)
- Set your client and secret from Step 1 in ``settings.py``::

    SOCIAL_AUTH_TEXASTRIBUNE_KEY = 'Your key here'
    SOCIAL_AUTH_TEXASTRIBUNE_SECRET = 'Your secret here'

- Add the following to your ``TEMPLATE_CONTEXT_PROCESSORS`` (in Django 1.8 and higher, this goes in ``TEMPLATES['OPTIONS']['context_processors']``)::

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

- Add the following to your ``urls.py``::

    url('', include('social.apps.django_app.urls', namespace='social')),

- Optional: if you don't want admins in Texas Tribune to be admins in this app, set ``AUTHENTICATE_TEXASTRIBUNE_STAFF=False`` in your Django settings or env var.
- Optional: if you are testing with a non-production version of the Texas Tribune app, you can set ``TEXASTRIBUNE_BASE_URL`` in your `settings.py`. For instance, if you want to test against a local server, you could set it to ``http://local.texastribune.org:8000/``.
- Optional: you may want to set a ``LOGIN_REDIRECT_URL``, which is where the login will redirect when complete.

Test it out by navigating to ``/login/texastribune`` and confirm that it goes through the whole handshake and drops you off at the ``LOGIN_REDIRECT_URL``.

.. _Django docs: https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#specifying-authentication-backends

Development & Tests
-------------------

To install and run tests::

    pip install -e .[test]
    py.test
