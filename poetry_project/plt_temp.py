import matplotlib.pyplot as plt
import pandas as pd
import requests


def build_dataframe(times, temperatures):
    df = pd.DataFrame({
        "time": pd.to_datetime(times),
        "temperature_c": temperatures,
    })
    return df.sort_values("time").reset_index(drop=True)


def main():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.75,
        "longitude": 37.61,
        "hourly": "temperature_2m",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    times = data["hourly"]["time"][:24]
    temperatures = data["hourly"]["temperature_2m"][:24]
    df = build_dataframe(times, temperatures)

    df.to_csv("temperature_24h.csv", index=False)

    fig, ax = plt.subplots()
    ax.plot(df["time"], df["temperature_c"], marker="o")
    ax.set_title("Температура в Москве (24 часа)")
    ax.set_xlabel("Время")
    ax.set_ylabel("°C")
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig("temperature_24h.png")
    plt.close(fig)

    print("Сохранены temperature_24h.csv и temperature_24h.png")


if __name__ == "__main__":
    main()