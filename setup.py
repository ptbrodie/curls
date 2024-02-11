from distutils.core import setup
from setuptools import find_packages


setup(name='curls',
      version='0.0.1',
      description='A command-line alternative to Postman.',
      url='http://github.com/ptbrodie/curls',
      author='Patrick Brodie',
      author_email='ptbrodie@gmail.com',
      packages=find_packages("."),
      install_requires=[
	  'certifi==2024.2.2',
	  'charset-normalizer==3.3.2',
	  'dateparser==1.2.0',
	  'idna==3.6',
	  'peewee==3.17.1',
	  'python-dateutil==2.8.2',
	  'pytz==2024.1',
	  'regex==2023.12.25',
	  'requests==2.31.0',
	  'six==1.16.0',
	  'terminaltables==3.1.10',
	  'tzlocal==5.2',
	  'urllib3==1.26.18'
      ],
      scripts=['./curls'])
