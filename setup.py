import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
# Don't import analytics-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'meergo','analytics'))
from version import VERSION

install_requires = [
    "requests~=2.7",
    "backoff~=2.1",
    "python-dateutil~=2.2",
    "PyJWT~=2.8.0"
]

tests_require = [
    "mock==2.0.0",
    "pylint==2.8.0",
    "flake8==3.7.9",
]

setup(
    name='meergo-analytics-python',
    version=VERSION,
    packages=['meergo.analytics', 'meergo.analytics.test'],
    python_requires='>=3.6.0',
    license='MIT License',
    install_requires=install_requires,
    extras_require={
        'test': tests_require
    },
)
