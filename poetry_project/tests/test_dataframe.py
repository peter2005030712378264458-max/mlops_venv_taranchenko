import pandas as pd

from plt_temp import build_dataframe


def test_build_dataframe():
    times = [
        "2026-10-27T02:00",
        "2026-10-27T00:00",
        "2026-10-27T01:00",
    ]
    temperatures = [3.2, 3.7, 3.4]

    df = build_dataframe(times, temperatures)

    assert df.columns.tolist() == ["time", "temperature_c"]
    assert len(df) == 3
    assert df["time"].tolist() == pd.to_datetime([
        "2026-10-27T00:00",
        "2026-10-27T01:00",
        "2026-10-27T02:00",
    ]).tolist()
    assert df["temperature_c"].tolist() == [3.7, 3.4, 3.2]