# noaastn

![](https://github.com/UBC-MDS/noaastn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/noaastn/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/noaastn) ![Release](https://github.com/UBC-MDS/noaastn/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/noaastn/badge/?version=latest)](https://noaastn.readthedocs.io/en/latest/?badge=latest)

Python package that downloads, processes and visualizes weather data from NOAA website.

## Features

- `get_data`:
  - This function downloads and save the data from <ftp://ftp.ncei.noaa.gov/pub/data/noaa/> based on station number and year

## Dependencies

[tool.poetry.dependencies]

- python = "^3.8"

[tool.poetry.dev-dependencies]

- pytest = "^6.2.2"
- pytest-cov = "^2.11.1"
- codecov = "^2.1.11"
- python-semantic-release = "^7.15.0"
- flake8 = "^3.8.4"
- Sphinx = "^3.5.1"
- sphinxcontrib-napoleon = "^0.7"

## Related Packages

- TODO

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/noaastn/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
