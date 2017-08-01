#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


def read(filename):
    with open(filename, "r") as f:
        return f.read()


NAME = 'snmpagent'


setup(
    name=NAME,
    version=__import__(NAME).__version__,
    description=(
        'Dell-EMC SNMP agent.'
    ),
    long_description=read('README.rst'),
    author='Ryan Liang',
    author_email='ryan.liang@dell.com',
    maintainer='Ryan Liang',
    maintainer_email='ryan.liang@dell.com',
    license='Apache Software License',
    packages=find_packages(exclude=('snmpagent.tests',)),
    package_dir={NAME: NAME},
    package_data={NAME: ['configs/*.conf']},
    platforms=["all"],
    url='http://github.com/emc-openstack/{}'.format(NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],

    install_requires=read('requirements.txt').splitlines(),
    tests_require=read('test-requirements.txt').splitlines(),
    entry_points={
        'console_scripts': [
            '{name}={name}.cli:main'.format(name=NAME),
        ],
    },
    scripts=[],
)
