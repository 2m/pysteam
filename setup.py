import uuid

from setuptools import setup
from pip.req import parse_requirements

import versioneer

requirements = [str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid1())]

DATA_FILES = [
  'requirements.txt',
  'versioneer.py',
]

TEST_DEPS = [
  'nose',
  'nose-parameterized',
  'mock',
]

setup(
  name='pysteam',
  version=versioneer.get_version(),
  cmdclass=versioneer.get_cmdclass(),
  description='Python library to work with Steam',
  url='http://github.com/scottrice/pysteam',
  author='Scott Rice',
  author_email='',
  license='MIT',
  packages=['pysteam'],
  install_requires=requirements,
  data_files=DATA_FILES,
  dependency_links=[
  ],
  zip_safe=False,
  test_suite='nose.collector',
  tests_require=TEST_DEPS,
  extras_require={'test': TEST_DEPS},
)
