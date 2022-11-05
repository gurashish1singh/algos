#!/bin/bash
set -eou pipefail

echo "Starting local setup"
echo "Installing poetry"
poetry install

echo -e "\nInstalling hooks"
# By default this is installed as a pre-commit hook
poetry run pre-commit install
