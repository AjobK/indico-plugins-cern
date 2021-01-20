# This file is part of the CERN Indico plugins.
# Copyright (C) 2014 - 2021 CERN
#
# The CERN Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License; see
# the LICENSE file for more details.

from setuptools import find_packages, setup


setup(
    name='indico-plugin-ravem',
    version='3.0-dev',
    url='https://github.com/indico/indico-plugins-cern',
    license='MIT',
    author='Indico Team',
    author_email='indico-team@cern.ch',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'indico>=3.0.dev0',
        'indico-plugin-vc-zoom>=2.3b1,<2.4.dev0',
    ],
    python_requires='~=3.9',
    entry_points={
        'indico.plugins': {'ravem = indico_ravem.plugin:RavemPlugin'},
    },
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
