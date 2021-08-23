"""
@author: Gabriele Girelli
@contact: gigi.ga90@gmail.com
"""

from clickomplete.scripts import autocomplete, clicko

import logging
from rich.logging import RichHandler  # type: ignore

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(markup=True, rich_tracebacks=True)],
)

__all__ = [
    "autocomplete",
    "clicko",
]
