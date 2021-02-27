def get_stations_info(country="US", path=None):
    """Downloads and cleans the data of all stations available at ftp://ftp.ncei.noaa.gov/pub/data/noaa/

    Parameters
    ----------
    country : str, optional
              Filters station information by country location that is represented by two character country code or "all" for every country, by default "US"
    path : str, optional
           path of the directory to save the data file. for example: "home/project/",
           defaults to None that does not save the file.

    Returns
    -------
    pandas.DataFrame
        Data frame containing information of all stations

    Examples
    --------
    >>> get_stations_info(country="US", path="home/project/")
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


def plot_weather_data(observations_df, y_axis, time_basis):
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
           chooses on the timely basis

    Examples
    --------
    >>> plot_data(observations_df, y_axis = airtemp, time_basis = monthly)
    """
