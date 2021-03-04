from ftplib import FTP
import gzip
import io
import pandas as pd
import numpy as np


def get_stations_info(country="US", path=None):
    """
    Downloads and cleans the data of all stations available at
    'ftp://ftp.ncei.noaa.gov/pub/data/noaa/'.

    Parameters
    ----------
    country : str, optional
        Filters station information by country location that is represented by
        two character country code or "all" for every country, by default "US".
    path : str, optional
        Path of the directory to save the data file. For example:
        "home/project/", defaults to None that does not save the file.

    Returns
    -------
    pandas.DataFrame
        Data frame containing information of all stations.

    Examples
    --------
    >>> get_stations_info(country="US", path="home/project/")
    """


def get_weather_data(station_number, year):
    """
    Loads and cleans weather data for a given NOAA station ID and year.
    Returns a dataframe containing a time series of air temperature (degrees
    Celsius), atmospheric pressure (hectopascals), wind speed (m/s), and wind
    direction (angular degrees). Also saves a copy of the raw data file
    downloaded from the NOAA FTP server at 'ftp.ncei.noaa.gov/pub/data/noaa/'.

    Parameters
    ----------
    station_number : str
        NOAA station number.
    year : int
        Year for which weather data should be returned

    Notes
    -----
        `station_number` is a combination of the USAF station ID and the NCDC
        WBAN number in the form '<USAF ID>-<WBAN ID>'.  If a WBAN ID does not
        exist, a value of '99999' should be used in its place.
        Example with WBAN ID - '911650-22536'
        Example without WBAN ID - '010015-99999'

        Station numbers can be found in the dataframe returned by
        `get_stations_info()` or through the NOAA's graphical tool at
        https://gis.ncdc.noaa.gov/maps/ncei/cdo/hourly

    Returns
    -------
    observations_df : pandas.DataFrame
        A dataframe that contains a time series of weather station
        observations.

    Examples
    --------
    >>> get_weather_data('911650-22536', 2020)
    """
    # Generate filename based on selected station number and year and download
    # data from NOAA FTP site.
    filename = station_number + "-" + str(year) + ".gz"

    noaa_ftp = FTP("ftp.ncei.noaa.gov")
    noaa_ftp.login()  # Log in (no user name or password required)
    noaa_ftp.cwd("pub/data/noaa/" + str(year) + "/")

    compressed_data = io.BytesIO()
    noaa_ftp.retrbinary("RETR " + filename, compressed_data.write)

    noaa_ftp.quit()

    # Unzip and process data line by line and extract variables of interest
    # The raw data file format is described here:
    # ftp://ftp.ncei.noaa.gov/pub/data/noaa/isd-format-document.pdf
    compressed_data.seek(0)
    stn_year_df = pd.DataFrame(
        columns=["stn", "datetime", "air_temp", "atm_press", "wind_spd", "wind_dir"]
    )
    with gzip.open(compressed_data, mode="rt") as stn_data:
        for i, line in enumerate(stn_data):
            stn_year_df.loc[i, "datetime"] = pd.to_datetime(line[15:27])
            stn_year_df.loc[i, "air_temp"] = float(line[87:92]) / 10
            stn_year_df.loc[i, "atm_press"] = float(line[99:104]) / 10
            stn_year_df.loc[i, "wind_spd"] = float(line[65:69]) / 10
            stn_year_df.loc[i, "wind_dir"] = float(line[60:63])

    # Replace missing value indicators with NaNs
    stn_year_df = stn_year_df.replace([999, 999.9, 9999.9], [np.nan, np.nan, np.nan])

    stn_year_df.loc[:, "stn"] = station_number
    return stn_year_df


def plot_weather_data(observations_df, y_axis, time_basis):
    """
    Visualizes the weather station observations including air temperature,
    atmospheric pressure, wind speed, and wind direction changing over time.

    Parameters
    ----------
    observations_df : pandas.DataFrame
        A dataframe that contains a time series of weather station
        observations.
    y_axis : str
        Variables that users would like to plot on a timely basis.
    time_basis : str
        The users can choose to plot the observations on yearly, monthly or
        daily basis

    Returns
    -------
    plot : `altair`
        A plot can visualize the changing of observation on the timely basis
        that user chooses.

    Examples
    --------
    >>> plot_weather_data(observations_df, y_axis=airtemp, time_basis=monthly)
    """
