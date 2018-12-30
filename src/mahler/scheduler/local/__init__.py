# -*- coding: utf-8 -*-
"""
:mod:`mahler.scheduler.local -- TODO
====================================

.. module:: local
    :platform: Unix
    :synopsis: TODO

TODO: Write long description
"""
from ._version import get_versions
from .resources import LocalResources, CPU_COUNT

VERSIONS = get_versions()
del get_versions

__descr__ = 'TODO'
__version__ = VERSIONS['version']
__license__ = 'GNU GPLv3'
__author__ = u'Xavier Bouthillier'
__author_short__ = u'Xavier Bouthillier'
__author_email__ = 'xavier.bouthillier@umontreal.ca'
__copyright__ = u'2018, Xavier Bouthillier'
__url__ = 'https://github.com/bouthilx/mahler.scheduler.local'


def build(processes=CPU_COUNT, **kwargs):
    return LocalResources(processes=processes)


def build_parser(parser):
    """Return the parser that needs to be used for this command"""
    local_parser = parser.add_parser('local', help='local help')

    local_parser.add_argument(
        '--processes', type=int, default=CPU_COUNT,
        help='number of concurrent process to spawn. Default: number of CPUs available')
