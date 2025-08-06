#!/usr/bin/env python3

import io
import os
from setuptools import find_packages, setup

# Where are we?
IS_DEA_SANDBOX = ('sandbox' in os.getenv('JUPYTER_IMAGE', default=''))

# What packages are required for this plugin to work
REQUIRED = [
    'xarray',
    'numba',
    'numpy',
    'datacube',
    'pyproj',
    'fsspec',
    'odc-stats',
    'odc-stac',
    'odc-io',
    'odc-algo',
    'odc-dscache',
    'pandas',
    'typing',
    'geopandas',
    'gdal',
    'scipy',
    'dask',
    'dask-ml',
    'geopy',
    'dea_tools'
]

#package metadata

NAME = 'fc-sub-annual-tools'
DESCRIPTION = 'Tools for generating sub-annual fractional cover'
URL = 'https://github.com/GeoscienceAustralia/dea-notebooks'
EMAIL = 'jenna.guffogg@ga.gov.au'
AUTHOR = 'Digital Earth Australia'
REQUIRES_PYTHON= '>=3.9.0'

setup_kwargs = {
    'name': NAME,
    'version': '0.0.1',
    'description': DESCRIPTION,
    'author': AUTHOR,
    'author_email': EMAIL,
    'python_requires': REQUIRES_PYTHON,
    'url': URL,
    'install_reqires': REQUIRED if not IS_DEA_SANDBOX else [],
    'packages': find_packages(),
    'include_package_date': True,
    'license': 'Apache License 2.0',
    'entry_points':{
        'console_scripts':[
            'cm-task = cm_tools.geojson_defined_tasks:main'
        ]
    },
}

setup(**setup_kwargs)