from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='tt_social_auth',
      version='0.0.1.dev1',
      description=u"Social auth backend for the Texas Tribune",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Liam Andrew",
      author_email='landrew@texastribune.org',
      url='https://github.com/texastribune/tt_social_auth',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'python-social-auth==0.2.14',
      ],
      extras_require={
          'test': ['pytest', 'httpretty', 'unittest2'],
      }
      )
