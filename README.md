# noaastn

![Buildbadge](https://github.com/UBC-MDS/noaastn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/noaastn/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/noaastn) [![Deploy](https://github.com/UBC-MDS/noaastn/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/noaastn/actions/workflows/deploy.yml) [![Documentation Status](https://readthedocs.org/projects/noaastn/badge/?version=latest)](https://noaastn.readthedocs.io/en/latest/?badge=latest)

The US National Oceanic and Atmospheric Administration (NOAA) collects and provides access to weather data from land-based weather stations within the US and around the world ([Land-Based Station Data](https://www.ncdc.noaa.gov/data-access/land-based-station-data)).  One method for accessing these data is through a publicly accessible FTP site.  This package allows users to easily download data from a given station for a given year, extract several key weather parameters from the raw data files, and visualize the variation in these parameters over time.  The weather parameters that are extracted with this package are:

- Air Temperature (degrees Celsius)
- Atmospheric Pressure (hectopascals)
- Wind Speed (m/s)
- Wind Direction (angular degrees)

## Installation
This package can be installed from TestPyPI by running the following command in a terminal

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple noaastn
```
## Features

- `get_stations_info`:
  - This function downloads and cleans the data of all stations available at <ftp://ftp.ncei.noaa.gov/pub/data/noaa/>
- `get_weather_data`:
  - This function loads and cleans weather data for a given NOAA station ID and year. It returns a dataframe containing a time series of air temperature, atmospheric pressure, wind speed, and wind direction.
- `plot_weather_data`:
  - This function visualizes the weather station observations including air temperature, atmospheric pressure, wind speed, and wind direction changing over time.

## Dependencies

The list of the dependencies for this package can be viewed under
`[tool.poetry.dependencies]` in 
[pyproject.toml](https://github.com/UBC-MDS/noaastn/blob/main/pyproject.toml)

## Related Packages

  There are few packages in the python ecosystem like [noaa](https://pypi.org/project/noaa/), [noaa-coops](https://pypi.org/project/noaa-coops/), [noaa-sdk](https://pypi.org/project/noaa-sdk/) that do analysis related to NOAA weather station data. These tools are more focused on using the NOAA's [API service](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation) to obtain forecast information. They do not provide an interface to obtain historical weather data from the NOAA's FTP site, process and visualize key weather parameters like this package does.

## Usage

Typical usage will begin with downloading the list of available weather stations in the country of interest using the `get_stations_info()` function.  A dataframe is returned which can be reviewed to find a suitable station in the area of interest.  Alternatively, the NOAA provides a [graphical interface](https://gis.ncdc.noaa.gov/maps/ncei/cdo/hourly) for exploring the available weather stations.

```python
>>> from noaastn import noaastn
>>> noaastn.get_stations_info(country = "US")
```

![Tabular output from get_stations_info function](https://raw.githubusercontent.com/UBC-MDS/noaastn/main/img/get_stations_info.png)

After selecting a weather station number, the `get_weather_data()` function can be used to download various weather parameters for the station number and year of interest.  NOAA stations are specified using two ID codes: the USAF station ID and the NCDC WBAN number.  The `station_number` argument must have the form '<USAF ID>-<WBAN ID>', both of which can be found in the table returned by `get_stations_info()` (if a WBAN ID does not exist, a value of '99999' should be used in its place).  The following usage example downloads weather data from station number "911650-22536" for the year 2020 and saves the data to a variable called 'weather_data'.  'weather_data' will be a data frame containing a time series of the following parameters for the station and year of interest:

- air temperature (degrees Celsius)
- atmospheric pressure (hectopascals)
- wind speed (m/s)
- wind direction (angular degrees)

```python
>>> weather_data = noaastn.get_weather_data("911650-22536", 2020)
>>> print(weather_data)
```

![Tabular output from get_weather_data function](https://raw.githubusercontent.com/UBC-MDS/noaastn/main/img/get_weather_data.png)

The function `plot_weather_data()` can be used to visualize a time series of any of the available weather parameters either on a mean daily or mean monthly basis.  The function returns an Altair chart object which can be saved or displayed in any environment which can render Altair objects.

```python
>>> noaastn.plot_weather_data(weather_data, col_name="air_temp", time_basis="monthly")
```

![Altair chart with time series of air temperature](https://raw.githubusercontent.com/UBC-MDS/noaastn/main/img/plot_weather_data.png)

## Documentation

Documentation for this package can be found on [Read the Docs](https://noaastn.readthedocs.io/en/latest/)

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/noaastn/graphs/contributors).  The package was originally developed by Chen Zhao, Chirag Rank, and Steffen Pentelow.

## Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
