import io
import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='zopyx.blockchain',
      version=version,
      description="ZOPYX blockchain ",
      long_description=io.open(os.path.join("docs", "source", "README.rst"), encoding='utf8').read() + "\n" +
      io.open(os.path.join("docs", "source", "HISTORY.rst"), encoding='utf8').read(),
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      author='Andreas Jung',
      author_email='info@zopyx.com',
      url='http://pypi.python.org/pypi/zopyx.blockchain',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopyx'],
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest', 'tox'],
      test_suite='tests',
      install_requires=[
          'lxml<4',
          'setuptools',
      ],
      )
