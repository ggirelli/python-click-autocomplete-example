"""
@author: Gabriele Girelli
@contact: gigi.ga90@gmail.com
"""

import click  # type: ignore
from clickomplete import __version__
from clickomplete.const import CONTEXT_SETTINGS
import webbrowser
import sys


@click.group(
    name="radiant",
    context_settings=CONTEXT_SETTINGS,
    help=f"""\b
Version:    {__version__}
Author:     Gabriele Girelli
Docs:       http://github.com/python-click-autocomplete-example
Code:       http://github.com/ggirelli/python-click-autocomplete-example

Radial Image Analisys Toolkit (RadIAnTkit) is a Python3.6+ package containing
tools for radial analysis of microscopy image.""",
)
@click.version_option(__version__)
def main() -> None:
    pass


@click.command(
    "_docs",
    help="Open online documentation on your favorite browser.",
)
def open_documentation() -> None:
    webbrowser.open("https://github.com/python-click-autocomplete-example/")
    sys.exit()


@click.command(
    "command_1",
    help="Does something.",
)
def command_1():
    pass


@click.command(
    "command_2",
    help="Does something else.",
)
def command_2():
    pass


main.add_command(open_documentation)
main.add_command(command_1)
main.add_command(command_2)


@click.group(
    name="subgroup_1",
    context_settings=CONTEXT_SETTINGS,
    help="Groups some sub-commands.",
)
def subgroup_1():
    pass


@click.command(
    "command_1",
    help="Does something new.",
)
def subgroup_1_command_1():
    pass


subgroup_1.add_command(subgroup_1_command_1)
main.add_command(subgroup_1)
