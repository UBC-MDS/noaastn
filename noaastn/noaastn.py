def get_data(station_number, year, path=None):
    """Download and save the data from ftp://ftp.ncei.noaa.gov/pub/data/noaa/ based on station number and year

    Args:
        station_number (str): The station number. for example: '010015-99999' represents BRINGELAND
        year (int): The year of the data collected at the station
        path (str, optional): path of the directory to save the data file. for example: "home/project/"
                              Defaults to None that is root location of the repository
    """

def process_data(path=None):
    """Extracts and cleans a time series of air temperature, atmospheric pressure, wind speed, and wind
    direction from raw data file and returns a dataframe.


    Args:
    path (str, optional): The path of the directory where raw data file is saved. Defaults value (None) assumes
    that the raw data is in the root of the repository.

    Returns:
    observations_df: (pandas.core.frame.DataFrame) Dataframe containing a time series of weather station observations
    """

    return observations_df

