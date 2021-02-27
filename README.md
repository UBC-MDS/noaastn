# noaastn

![](https://github.com/UBC-MDS/noaastn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/noaastn/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/noaastn) ![Release](https://github.com/UBC-MDS/noaastn/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/noaastn/badge/?version=latest)](https://noaastn.readthedocs.io/en/latest/?badge=latest)

The US National Oceanic and Atmospheric Administration (NOAA) collects and provides access to weather data from land-based weather stations within the US and around the world ([link](https://www.ncdc.noaa.gov/data-access/land-based-station-data)).  One method for accessing these data is through a publically accessible FTP site.  This package allows users to easily download data from a given station for a given year, extract several key weather parameters from the raw data files, and visualize the variation in these parameters over time.  The weather parameters that are extracted with this package are:

- Air Temperature (degrees Celsius)
- Atmospheric Pressure (hectopascals)
- Wind Speed (m/s)
- Wind Direction (angular degrees)

## Features

- `get_stations_info`:
  - This function downloads and cleans the data of all stations available at <ftp://ftp.ncei.noaa.gov/pub/data/noaa/>
- `process_data`:
  - This function extracts and cleans a time series of air temperature, atmospheric pressure, wind speed, and wind direction from raw data file and returns a dataframe.
- `plot_weather_data`:
  - This function visualizes the weather station observations including air temperature, atmospheric pressure, wind speed, and wind direction changing with time and returns a line plot.

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

  There are few packages in the python ecosystem like [noaa](https://pypi.org/project/noaa/), [noaa-coops](https://pypi.org/project/noaa-coops/), [noaa-sdk](https://pypi.org/project/noaa-sdk/) that does analysis related to the NOAA station data. However, the tools are more focused on using [API service](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation) for getting the forecast information and does not use similar method to get the historical weather data related to a particular station.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/noaastn/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
