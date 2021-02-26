import numpy as np
import pandas as pd
import altair as alt


def get_data(station_number, year, path=None):
    """
    Download and save the data from ftp://ftp.ncei.noaa.gov/pub/data/noaa/
    based on station number and year.

    Parameters
    ----------
    station_number : str
                     The station number. for example: '010015-99999'
                     represents BRINGELAND
    year : int
           The year of the data collected at the station
    path : str, optional
           path of the directory to save the data file. for example:
           "home/project/", defaults to None that is root location of
           the repository
    """


def process_data(path=None):
    """
    Extracts and cleans a time series of air temperature, atmospheric pressure,
    wind speed, and wind direction from raw data file and returns a dataframe.

    Parameters
    ----------
    path : str, optional
           The path of the directory where raw data file is saved. Defaults
           value (None) assumes that the raw data is in the root of the
           repository.

    Returns
    -------
    observations_df : pandas.core.frame.DataFrame
                      Dataframe containing a time series of weather station
                      observations
    """

    return observations_df


def plot_data(observations_df, y_axis, time_basis):
    """Visualize the weather station observations including air temperature,
    atmospheric pressure, wind speed, and wind direction changing with time
    and return a line plot.

    Parameters
    ----------
    observations_df : pandas.core.frame.DataFrame
                      Dataframe containing a time series of weather station
                      observations
    y_axis : str
             Variables that users would like to plot on a timely basis
    time_basis : str
                 The users can choose to plot the observations on yearly,
                 monthly or daily basis

    Returns
    -------
    plot : `altair`
           A line plot that visualizes the changing of observation user
           chooses on the timly basis

    Examples
    --------
    >>> plot_data(observations_df, y_axis = airtemp, time_basis = montly)
    """
