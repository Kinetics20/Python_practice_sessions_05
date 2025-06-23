import requests


def get_random_genres(n: int = 1) -> list[str]:
    """
    Get `n` random music genres from BinaryJazz Genrenator API.
    Docs: https://binaryjazz.us/
    """
    url = f"https://binaryjazz.us/wp-json/genrenator/v1/genre/{n}"
    response = requests.get(url)
    response.raise_for_status()
    genres = response.json()
    return genres if isinstance(genres, list) else [genres]


def get_random_got_quote() -> dict[str, object]:
    """
    Get a random quote from Game of Thrones API.
    Docs: https://gameofthronesquotes.xyz/
    """
    url = "https://api.gameofthronesquotes.xyz/v1/random"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def convert_bng_to_latlong(easting: int, northing: int) -> dict[str, float]:
    """
    Convert BNG (British National Grid) coordinates to lat/long.
    """
    url = f"https://api.getthedata.com/bng2latlong/{easting}/{northing}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "ok":
        raise ValueError(f"No match found for coordinates: {easting}, {northing}")

    return {
        "latitude": float(data["latitude"]),
        "longitude": float(data["longitude"])
    }




def get_satellite_data(int_des: str) -> list[dict[str, object]]:
    """
    Get satellite orbital data from CelesTrak by international designator (INTDES).
    Docs: https://celestrak.org/NORAD/documentation/gp-data-formats.php
    """
    url = f"https://celestrak.org/NORAD/elements/gp.php?INTDES={int_des}&FORMAT=JSON-PRETTY"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("🎵 Genres:", get_random_genres(3))
    print("🗡 GOT Quote:", get_random_got_quote())
    print("📍 BNG → LatLong:", convert_bng_to_latlong(651409, 313177))
    print("🚀 CelesTrak Data:", get_satellite_data("2023-015"))
