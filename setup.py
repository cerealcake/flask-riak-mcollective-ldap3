from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='data',
      version='0.0.1',
      description=u"riak-api",
      long_description='Riak KV api wrapper',
      classifiers=[],
      keywords='',
      author=u"Jaime Viloria",
      author_email='jaimeviloria@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'flask',
          'riak',
          'click',
          'requests',
          'ldap3'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      riak_http=app.lib.http_controller:run
      riak_cli=app.cli.v1:cli
      """
      )
