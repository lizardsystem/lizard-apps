import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'Django',
]

setup(
    name='lizard-apps',
    version='0.2.10',
    packages=['lizard_apps'],
    include_package_data=True,
    license='MIT License',
    description='A simple Google-apps like Django app.',
    long_description=README,
    url='',
    author='nens',
    author_email='info@nelen-schuurmans.nl',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
