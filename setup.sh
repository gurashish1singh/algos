echo "Starting local setup"
echo "Installing poetry"
poetry install

echo "Installing hooks "
poetry run pre-commit install
