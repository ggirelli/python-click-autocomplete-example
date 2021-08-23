"""
@author: Gabriele Girelli
@contact: gigi.ga90@gmail.com
"""

from importlib.metadata import version
from typing import List

try:
    __version__ = version(__name__)
except Exception as e:
    raise e

__all__ = ["__version__"]
__path__: List[str]
