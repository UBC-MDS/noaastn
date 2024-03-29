from noaastn import noaastn
import pandas as pd

station_number = "911803-99999"
year = 2015
weather_df = noaastn.get_weather_data(station_number, year)


def test_output_type():
    assert (
        type(weather_df) == pd.core.frame.DataFrame
    ), "Weather data should be returned as a Pandas DataFrame."


def test_output_shape():
    assert (
        weather_df.shape[0] == 6
    ), "Test data should have 6 rows (observations)."
    assert weather_df.shape[1] == 6, "Dataframe should have 6 columns."


def test_column_datatypes():
    assert (
        weather_df.datetime.dtype == "<M8[ns]"
    ), "Data type of datetime column is incorrect (should be'<M8[ns]')."
    assert (
        weather_df.air_temp.dtype == "float64"
    ), "Data type of air_temp column is incorrect (should be 'float64')."
    assert (
        weather_df.atm_press.dtype == "float64"
    ), "Data type of atm_press column is incorrect (should be 'float64')."
    assert (
        weather_df.wind_spd.dtype == "float64"
    ), "Data type of wind_spd column is incorrect (should be 'float64')."
    assert (
        weather_df.wind_dir.dtype == "float64"
    ), "Data type of wind_dir column is incorrect (should be 'float64')."


def test_station_number_coding():
    assert (
        weather_df.stn.unique().shape[0] == 1
    ), "There should only be one station number in the data table"
    assert (
        weather_df.stn.unique()[0] == station_number
    ), "Station number should match entries values in stn column"


def test_ftp_error_handling():
    assert (
        not noaastn.get_weather_data("999999-99999", 1750)
    ), """Entry of invalid station/year combination should not return
    anything."""
