import gzip
import io
import os
import re
from ftplib import FTP

import numpy as np
import pandas as pd
import altair as alt


def get_stations_info(country="all"):
    """
    Downloads and cleans the data of all stations available at
    'ftp://ftp.ncei.noaa.gov/pub/data/noaa/'.

    Parameters
    ----------
    country : str, optional
        Filters station information by country location that is represented by
        two character country code("US") or "all" for every country, by default "all".

    Returns
    -------
    pandas.DataFrame
        Data frame containing information of all stations.

    Examples
    --------
    >>> get_stations_info(country="US")
    """

    # Get station info file from the ftp site
    ftp_address = "ftp.ncei.noaa.gov"
    ftp_dir = "pub/data/noaa/"
    stn_history_file = "isd-history.txt"  # station information/history file.
    columns = [
        "usaf",
        "wban",
        "stn_name",
        "country",
        "state",
        "call",
        "lat",
        "lon",
        "elevation",
        "start",
        "end",
    ]
    col_index = [0, 7, 13, 43, 48, 51, 57, 65, 74, 82, 91, 101]
    skip_lines = 21

    # connect, login and change working directory to /pub/data/noaa/
    noaa_ftp = FTP(ftp_address)
    noaa_ftp.login()
    noaa_ftp.cwd(ftp_dir)

    # save file and quit
    with open(stn_history_file, "wb+") as stn_hist:
        noaa_ftp.retrbinary("RETR " + stn_history_file, stn_hist.write)
    noaa_ftp.quit()

    # create data_dic from the file
    data = [[] for i in range(len(col_index) - 1)]
    with open(stn_history_file, mode="rt") as stn_hist:
        for i, line in enumerate(stn_hist):
            if i <= skip_lines:
                continue
            for i in range(len(col_index) - 1):
                val = line[col_index[i] : col_index[i + 1]].strip()
                if len(val) > 0:
                    data[i].append(line[col_index[i] : col_index[i + 1]].strip())
                else:
                    data[i].append(None)

    os.remove("isd-history.txt")
    data_dic = {columns[i]: data[i] for i in range(len(data))}
    data_df = pd.DataFrame(data_dic)

    # datatype conversion of the datetime column
    data_df.start = pd.to_datetime(data_df.start)
    data_df.end = pd.to_datetime(data_df.end)

    # filter if the country parameter is valid
    if country != "all":
        print(len(country), len(country) != 2)
        if len(country) != 2 or not isinstance(country, str):
            raise Exception("Invalid country parameter")
        else:
            data_df = data_df[data_df["country"] == country]

    return data_df


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

    assert type(year) == int, "Year must be entered as an integer"
    assert type(station_number) == str, "Station number must be entered as a string"
    assert re.match(
        "^\d{6}[-]\d{5}$", station_number
    ), 'Station number must be entered in form "911650-22536".  See documentation for additional details.'

    # Generate filename based on selected station number and year and download
    # data from NOAA FTP site.
    filename = station_number + "-" + str(year) + ".gz"

    noaa_ftp = FTP("ftp.ncei.noaa.gov")
    noaa_ftp.login()  # Log in (no user name or password required)
    noaa_ftp.cwd("pub/data/noaa/" + str(year) + "/")

    compressed_data = io.BytesIO()

    try:
        noaa_ftp.retrbinary("RETR " + filename, compressed_data.write)
    except error_perm as e_mess:
        if re.search("(No such file or directory)", str(e_mess)):
            print("Data not available for that station number / year combination")
        else:
            print("Error generated from NOAA FTP site: \n")
        noaa_ftp.quit()

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


def plot_weather_data(obs_df, col_name, time_basis):
    """
    Visualizes the weather station observations including air temperature,
    atmospheric pressure, wind speed, and wind direction changing over time.
    Parameters
    ----------
    obs_df : pandas.DataFrame
        A dataframe that contains a time series of weather station
        observations.
    col_name : str
        Variables that users would like to plot on a timely basis,
        including air_temp, atm_press, wind_spd, wind_dir
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
    >>> plot_weather_data(obs_df, col_name="air_temp", time_basis="monthly")
    """

    # Test input types
    assert (
        type(obs_df) == pd.core.frame.DataFrame
    ), "Weather data should be a Pandas DataFrame."
    assert type(col_name) == str, "Variable name must be entered as a string"
    assert type(time_basis) == str, "Time basis must be entered as a string"
    # Test edge cases
    assert col_name in [
        "air_temp",
        "atm_press",
        "wind_spd",
        "wind_dir",
    ], "Variable can only be one of air_temp, atm_press, wind_spd or wind_dir"
    assert time_basis in ["monthly", "daily"], "Time basis can only be monthly or daily"

    df = obs_df.dropna()
    assert (
        len(df.index) > 2
    ), "Dataset is not sufficient to visualize"  # Test edge cases
    year = df.datetime.dt.year[0]

    if time_basis == "monthly":
        df = df.set_index("datetime").resample("M").mean().reset_index()
        assert (
            len(df.index) > 2
        ), "Dataset is not sufficient to visualize"  # Test edge cases

        if col_name == "air_temp":
            line = (
                alt.Chart(df, title="Air Temperature for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X(
                        "month(datetime)", title="Month", axis=alt.Axis(labelAngle=-30)
                    ),
                    alt.Y(
                        "air_temp", title="Air Temperature", scale=alt.Scale(zero=False)
                    ),
                    alt.Tooltip(col_name),
                )
            )
        elif col_name == "atm_press":
            line = (
                alt.Chart(df, title="Atmospheric Pressure for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X(
                        "month(datetime)", title="Month", axis=alt.Axis(labelAngle=-30)
                    ),
                    alt.Y(
                        "atm_press",
                        title="Atmospheric Pressure",
                        scale=alt.Scale(zero=False),
                    ),
                    alt.Tooltip(col_name),
                )
            )
        elif col_name == "wind_spd":
            line = (
                alt.Chart(df, title="Wind Speed for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X(
                        "month(datetime)", title="Month", axis=alt.Axis(labelAngle=-30)
                    ),
                    alt.Y("wind_spd", title="Wind Speed", scale=alt.Scale(zero=False)),
                    alt.Tooltip(col_name),
                )
            )
        else:
            line = (
                alt.Chart(df, title="Wind Direction for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X(
                        "month(datetime)", title="Month", axis=alt.Axis(labelAngle=-30)
                    ),
                    alt.Y(
                        "wind_dir", title="Wind Direction", scale=alt.Scale(zero=False)
                    ),
                    alt.Tooltip(col_name),
                )
            )

    else:
        df = df.set_index("datetime").resample("D").mean().reset_index()
        assert (
            len(df.index) > 2
        ), "Dataset is not sufficient to visualize"  # Test edge cases

        if col_name == "air_temp":
            line = (
                alt.Chart(df, title="Air Temperature for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X("datetime", title="Date", axis=alt.Axis(labelAngle=-30)),
                    alt.Y(
                        "air_temp", title="Air Temperature", scale=alt.Scale(zero=False)
                    ),
                    alt.Tooltip(col_name),
                )
            )
        elif col_name == "atm_press":
            line = (
                alt.Chart(df, title="Atmospheric Pressure for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X("datetime", title="Date", axis=alt.Axis(labelAngle=-30)),
                    alt.Y(
                        "atm_press",
                        title="Atmospheric Pressure",
                        scale=alt.Scale(zero=False),
                    ),
                    alt.Tooltip(col_name),
                )
            )
        elif col_name == "wind_spd":
            line = (
                alt.Chart(df, title="Wind Speed for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X("datetime", title="Date", axis=alt.Axis(labelAngle=-30)),
                    alt.Y("wind_spd", title="Wind Speed", scale=alt.Scale(zero=False)),
                    alt.Tooltip(col_name),
                )
            )
        else:
            line = (
                alt.Chart(df, title="Wind Direction for " + str(year))
                .mark_line(color="orange")
                .encode(
                    alt.X("datetime", title="Date", axis=alt.Axis(labelAngle=-30)),
                    alt.Y(
                        "wind_dir", title="Wind Direction", scale=alt.Scale(zero=False)
                    ),
                    alt.Tooltip(col_name),
                )
            )

    chart = (
        line.properties(width=500, height=350)
        .configure_axis(labelFontSize=15, titleFontSize=20, grid=False)
        .configure_title(fontSize=25)
    )

    return chart
