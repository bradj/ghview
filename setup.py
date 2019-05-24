__license__ = '''
This file is part of GHView.

GHView is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

GHView is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with GHView.  If not, see
<http://www.gnu.org/licenses/>.
'''
# pylint: disable=bad-whitespace

from setuptools import setup

import imp
_version = imp.load_source("ghview.version", "ghview/version.py")

long_description = open('README.md').read()


setup(
  name    = 'GHView',
  version = _version.__version__,
  author  = 'Brad Janke',
  author_email = 'brad@bradjanke.com',
  license = 'LICENSE',
  url     = 'http://github.com/bradj/ghview/',
  description      = 'GHView is a command line homework checking.',
  long_description = long_description,
  keywords         = 'github viewer organizations analytics',
  classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: PyPy',
  ],

  packages = ['ghview'],
  install_requires = ['click==7.0', 'requests==2.22.0', 'halo==0.0.23'],
  include_package_data = True,
  entry_points='''
        [console_scripts]
        ghview=ghview.cli:run
    '''
)
