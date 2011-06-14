#encoding:utf8
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='cremedeflux',
      version=version,
      description="Crème de Flux: Publish the cream of your lifestream",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      maintainer='Matthew Scott, ElevenCraft Inc.',
      maintainer_email='matt@11craft.com',
      url='https://github.com/cremedeflux/cremedeflux',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [cremedeflux_plugins]
      test_hourly = cdf.tests.plugins.hourly:HourlyPlugin
      """,
      )
