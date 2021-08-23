# python-click-autocomplete-example

This is an example on how to setup shell autocompletion in your python scripts reading input via [click](https://github.com/pallets/click/), especially when working on a Python package using [Poetry](https://github.com/python-poetry/poetry).

## Requirements

To test this example you will need:

* **Python v3.8+**
* **Poetry**

## Usage

Set up the example's environment and enter it with:

```bash
git clone https://github.com/ggirelli/python-click-autocomplete-example.git
cd python-click-autocomplete-example
poetry install
poetry shell
```

This example package provides you with two scripts:

* `clicko` is a placeholder mimicking a normal script with subcommands and commands.
* `clicko-autocomplete` can be used to enable autocompletion for the `clicko` script.

Currently, autocompletion is supported for `bash`, `fish`, and `zsh`. To activate it, simply run:

```bash
clicko-autocomplete -s SHELL_TYPE
```

The default `SHELL_TYPE` is `bash`.

Now, you should be able to test autocompletion by typing `clicko <TAB> <TAB>`.

## How does it work

The `clicko-autocomplete` script is able to generate and install shell autocompletion configuration files, stored by default in the `autocomplete` subfolder of this package. This is done by exploiting the in-built autocompletion tools served by `click`.

When installing the autocompletion configuration files for `bash` or `zsh`, the `clicko-autocomplete` script is able to check if the config files were already installed, and avoid re-installation.

To read more on autocompletion with `click`, check out [their documentation](https://click.palletsprojects.com/en/8.0.x/shell-completion/).
