from noaastn import noaastn

station_number = "713930-99999"
year = 2021
weather_df = noaastn.get_weather_data(station_number, year)
plot_at_m = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="air_temp", time_basis="monthly"
)
plot_ap_m = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="atm_press", time_basis="monthly"
)
plot_ws_m = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="wind_spd", time_basis="monthly"
)
plot_wd_m = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="wind_dir", time_basis="monthly"
)
plot_at_d = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="air_temp", time_basis="daily"
)
plot_ap_d = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="atm_press", time_basis="daily"
)
plot_ws_d = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="wind_spd", time_basis="daily"
)
plot_wd_d = noaastn.plot_weather_data(
    obs_df=weather_df, col_name="wind_dir", time_basis="daily"
)


def test_plot_weather_data():
    assert (
        plot_at_m.encoding.x.shorthand == "month(datetime)"
    ), "datetime should be mapped to the x axis"
    assert (
        plot_at_m.encoding.y.shorthand == "air_temp"
    ), "air_temp should be mapped to the y axis"
    assert (
        plot_ap_m.encoding.y.shorthand == "atm_press"
    ), "atm_press should be mapped to the y axis"
    assert (
        plot_ws_m.encoding.y.shorthand == "wind_spd"
    ), "wind_spd should be mapped to the y axis"
    assert (
        plot_wd_m.encoding.y.shorthand == "wind_dir"
    ), "wind_dir should be mapped to the y axis"
    assert (
        plot_at_d.encoding.x.shorthand == "datetime"
    ), "datetime should be mapped to the x axis"
    assert (
        plot_at_d.encoding.y.shorthand == "air_temp"
    ), "air_temp should be mapped to the y axis"
    assert (
        plot_ap_d.encoding.y.shorthand == "atm_press"
    ), "atm_press should be mapped to the y axis"
    assert (
        plot_ws_d.encoding.y.shorthand == "wind_spd"
    ), "wind_spd should be mapped to the y axis"
    assert (
        plot_wd_d.encoding.y.shorthand == "wind_dir"
    ), "wind_dir should be mapped to the y axis"
    assert plot_at_m.mark.type == "line", "mark should be a line"
    assert plot_at_m.mark.color == "orange", "mark color should be orange"
    assert (
        plot_at_m.encoding.x.axis.labelAngle == -30
    ), "x axis label shoudl oriented to -30 degree"
    assert plot_at_m.encoding.y.scale.zero == False, "y axis should not start at 0"
