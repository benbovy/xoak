from importlib.metadata import version

from xoak.accessor import XoakAccessor
from xoak.index import IndexAdapter, IndexRegistry
from xoak.tree_adapters import (
    S2PointTreeAdapter,
    SklearnBallTreeAdapter,
    SklearnGeoBallTreeAdapter,
    SklearnKDTreeAdapter,
)

__all__ = [
    "IndexAdapter",
    "IndexRegistry",
    "SklearnBallTreeAdapter",
    "SklearnGeoBallTreeAdapter",
    "SklearnKDTreeAdapter",
    "S2PointTreeAdapter",
    "XoakAccessor",
]

__version__ = version("xoak")
