import pandas as pd
import pytest
from noaastn import noaastn
from pandas.api.types import is_datetime64_any_dtype as is_datetime

get_stations_info_params = [("all", [29561, 253]), ("US", [7158, 1])]
invalid_params = ["XXX", 12]
num_column = 11

col_len = {
    "country": 2,
    "state": 2,
    "usaf": 6,
    "wban": 5,
    "latitude": 7,
    "longitude": 8,
    "elevation": 7,
}


@pytest.mark.parametrize("param, expected_output", get_stations_info_params)
def test_get_stations_info(param, expected_output):

    data_all = noaastn.get_stations_info(country=param)

    # check number of columns
    assert data_all.shape[1] == num_column

    # check type of the columns
    for i in range(9):
        assert data_all.dtypes[i] == object
    is_datetime(data_all["start"])
    is_datetime(data_all["end"])

    # match and check each col value pattern by comparing length
    row_df = data_all.sample(1)
    for col in col_len.keys():
        assert (
            pd.isna(row_df[col].values[0])
            or pd.isnull(row_df[col].values[0])
            or len(row_df[col].values[0]) == col_len[col]
        )


def test_get_stations_info_exception():
    with pytest.raises(Exception) as ex_info:
        assert noaastn.get_stations_info(country=12)
    assert (
        str(ex_info.value)
        == "Invalid country parameter. parameter should be a string"
    )

    with pytest.raises(Exception) as ex_info:
        assert noaastn.get_stations_info(country="XXX")
    assert (
        str(ex_info.value)
        == "Invalid country parameter. parameter should be length 2"
    )
