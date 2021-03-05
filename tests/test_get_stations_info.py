import pytest
from noaastn import __version__, noaastn
from pandas.api.types import is_datetime64_any_dtype as is_datetime

get_stations_info_params = [("all", [29560, 253]), ("US", [7157, 1])]
invalid_params = ["XXX", 12]
num_column = 11


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

    # check the number of columns and the number of countries in dataframe
    assert data_all.shape[0] == expected_output[0]
    assert len(set(data_all["country"])) == expected_output[1]


def test_get_stations_info_exception():
    for param in invalid_params:
        with pytest.raises(Exception) as ex_info:
            noaastn.get_stations_info(country=param)
            assert str(ex_info.value) == "Invalid country parameter"
