# noaastn

![](https://github.com/UBC-MDS/noaastn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/noaastn/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/noaastn) ![Release](https://github.com/UBC-MDS/noaastn/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/noaastn/badge/?version=latest)](https://noaastn.readthedocs.io/en/latest/?badge=latest)

The US National Oceanic and Atmospheric Administration (NOAA) collects and provides access to weather data from land-based weather stations within the US and around the world ([Land-Based Station Data](https://www.ncdc.noaa.gov/data-access/land-based-station-data)).  One method for accessing these data is through a publically accessible FTP site.  This package allows users to easily download data from a given station for a given year, extract several key weather parameters from the raw data files, and visualize the variation in these parameters over time.  The weather parameters that are extracted with this package are:

- Air Temperature (degrees Celsius)
- Atmospheric Pressure (hectopascals)
- Wind Speed (m/s)
- Wind Direction (angular degrees)

## Features

- `get_stations_info`:
  - This function downloads and cleans the data of all stations available at <ftp://ftp.ncei.noaa.gov/pub/data/noaa/>
- `get_weather_data`:
  - This function loads and cleans weather data for a given NOAA station ID and year. It returns a dataframe containing a time series of air temperature, atmospheric pressure, wind speed, and wind direction.
- `plot_weather_data`:
  - This function visualizes the weather station observations including air temperature, atmospheric pressure, wind speed, and wind direction changing over time.

## Dependencies

[tool.poetry.dependencies]

- python = "^3.8"
- pandas = "^1.2.3"
- altair = "^4.1.0"

[tool.poetry.dev-dependencies]

- pytest = "^6.2.2"
- pytest-cov = "^2.11.1"
- codecov = "^2.1.11"
- python-semantic-release = "^7.15.0"
- flake8 = "^3.8.4"
- Sphinx = "^3.5.1"
- sphinxcontrib-napoleon = "^0.7"

## Related Packages

  There are few packages in the python ecosystem like [noaa](https://pypi.org/project/noaa/), [noaa-coops](https://pypi.org/project/noaa-coops/), [noaa-sdk](https://pypi.org/project/noaa-sdk/) that do analysis related to NOAA weather station data. These tools are more focused on using the NOAA's [API service](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation) to obtain forecast information. They do not provide an interface to obtain historical weather data from the NOAA's FTP site, process and visualize key weather parameters like this package do.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/noaastn/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
