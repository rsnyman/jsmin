from setuptools import setup

import os
import re

# this disables including resource forks in tar files on os x
os.environ['COPYFILE_DISABLE'] = 'true'


def long_description():
    return open('README.rst').read() + '\n' + open('CHANGELOG.txt').read()


setup(
    name='jsmin',
    version=re.search(r'__version__ = ["\']([^"\']+)',
                      open('jsmin/__init__.py').read()).group(1),
    packages=['jsmin'],
    description='JavaScript minifier.',
    long_description=long_description(),
    author='Dave St.Germain',
    author_email='dave@st.germa.in',
    maintainer='Raoul Snyman',
    maintainer_email='raoul@snyman.info',
    test_suite='jsmin.test',
    license='MIT License',
    url='https://github.com/rsnyman/jsmin/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Text Processing :: Filters',
    ],
)
