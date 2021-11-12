#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Shekhar Tiwatne",
    author_email='pythonic@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Git Based Leaves management system",
    entry_points={
        'console_scripts': [
            'gitleaves=gitleaves.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='gitleaves',
    name='gitleaves',
    packages=find_packages(include=['gitleaves', 'gitleaves.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/scrollstack/gitleaves',
    version='0.2.0',
    zip_safe=False,
)