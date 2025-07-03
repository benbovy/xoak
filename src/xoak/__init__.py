from pkg_resources import DistributionNotFound, get_distribution

from xoak.accessor import XoakAccessor
from xoak.index import IndexAdapter, IndexRegistry
from xoak.tree_adapters import (
    S2PointTreeAdapter,
    SklearnBallTreeAdapter,
    SklearnGeoBallTreeAdapter,
    SklearnKDTreeAdapter,
)

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    pass

__all__ = [
    'IndexAdapter',
    'IndexRegistry',
    'SklearnBallTreeAdapter',
    'SklearnGeoBallTreeAdapter',
    'SklearnKDTreeAdapter',
    'S2PointTreeAdapter',
    'XoakAccessor',
]
