def get_data(station_number, year, path=None):
    """Download and save the data from ftp://ftp.ncei.noaa.gov/pub/data/noaa/ based on station number and year

    Args:
        station_number (str): The station number. for example: '010015-99999' represents BRINGELAND
        year (int): The year of the data collected at the station
        path (str, optional): path of the directory to save the dataframe. for example: "home/project/"
                              Defaults to None that is root location of the repository
    """