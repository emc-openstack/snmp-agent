#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


def read(filename):
    with open(filename, "r") as f:
        return f.read()


COMMAND_NAME = 'snmpagent-unity'

setup(
    name=COMMAND_NAME,
    version=__import__('snmpagent_unity').__version__,
    description=(
        'Dell EMC Unity SNMP Off-Array Agent.'
    ),
    long_description=read('README.rst'),
    author='Yong Huang',
    author_email='yong.huang@dell.com',
    maintainer='Yong Huang',
    maintainer_email='yong.huang@dell.com',
    license='Apache Software License',
    package_data={'snmpagent_unity': ['mib_files/*']},
    packages=find_packages(exclude=('snmpagent_unity.tests',
                                    'snmpagent_unity.comptests')),
    platforms=["all"],
    url='http://github.com/emc-openstack/{}'.format(COMMAND_NAME),
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

    install_requires=read('./requirements.txt').splitlines(),
    tests_require=read('./test-requirements.txt').splitlines(),
    entry_points={
        'console_scripts': [
            '{}=snmpagent_unity.cli:main'.format('snmpagent-unity'),
        ],
    },
    scripts=[],
)
