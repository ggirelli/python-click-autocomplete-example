"""
@author: Gabriele Girelli
@contact: gigi.ga90@gmail.com
"""

import click  # type: ignore
import os
from rich import print  # type: ignore
from shutil import copyfile
import sys

from clickomplete import __path__, __version__
from clickomplete.const import CONTEXT_SETTINGS


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--shell-type",
    "-s",
    help="shell type for which to activate autocompletion",
    type=click.Choice(["bash", "zsh", "fish"], case_sensitive=False),
    default="bash",
    show_default=True,
)
@click.option(
    "--regenerate",
    help="to regenerate autocompletion file, mainly for developers",
    type=click.BOOL,
    default=False,
    is_flag=True,
)
@click.version_option(__version__)
def main(shell_type: str, regenerate: bool) -> None:
    user_home_path = os.path.expanduser("~")
    autocomplete_path = os.path.join(
        __path__[0], "autocomplete", f".clicko-complete.{shell_type}"
    )

    if regenerate:
        regenerate_autocompletion_files(shell_type, autocomplete_path)

    if shell_type in ("bash", "zsh"):
        autocomplete_bash_or_zsh(user_home_path, autocomplete_path, shell_type)
    elif "fish" == shell_type:
        autocomplete_fish(user_home_path, autocomplete_path)

    print("Done. :thumbs_up: :smiley:")


def regenerate_autocompletion_files(shell_type: str, autocomplete_path: str) -> None:
    os.system(f"_CLICKO_COMPLETE={shell_type}_source clicko > {autocomplete_path}")
    print(f"Regenerated {shell_type} completion file: {autocomplete_path}")


def autocomplete_fish(user_home_path: str, autocomplete_path: str) -> None:
    destination_path = os.path.join(
        user_home_path, ".config/fish/completions/clicko.fish"
    )

    if os.path.isfile(destination_path):
        print("Autocompletion was previously set up. Skipping.")
        sys.exit()

    copyfile(
        autocomplete_path,
        destination_path,
    )


def autocomplete_bash_or_zsh(
    user_home_path: str, autocomplete_path: str, shell_type: str = "bash"
) -> None:
    assert shell_type in ("bash", "zsh")

    autocompletion_string = f". {autocomplete_path} # CLICKO-AUTOCOMPLETE\n"
    run_command_path = os.path.join(user_home_path, f".{shell_type}rc")

    with open(run_command_path, "r") as OH:
        if autocompletion_string in OH.readlines():
            print("Autocompletion was previously set up. Skipping.")
            sys.exit()

    with open(run_command_path, "a+") as OH:
        OH.write(f"\n{autocompletion_string}")
