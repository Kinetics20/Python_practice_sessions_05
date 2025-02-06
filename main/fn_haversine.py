from math import radians, sin, cos, sqrt, asin
from typing import TypeAlias

MI = 3959  # Statute miles
NM = 3440  # Nautical miles
KM = 6371  # Kilometers

Point: TypeAlias = tuple[float, float]

def haversine(p1: Point, p2: Point, r: float = NM) -> float:
    """
    Computes the great-circle distance between two points on a sphere
    using the haversine formula.

    Args:
        p1 (Point): Coordinates of the first point (latitude, longitude) in degrees.
        p2 (Point): Coordinates of the second point (latitude, longitude) in degrees.
        r (float, optional): Radius of the sphere in the chosen unit of measurement
                             (e.g., KM, MI, NM). Defaults to nautical miles (NM).

    Returns:
        float: The distance between the two points in the units specified by R.
    """
    lat_1, lon_1 = p1
    lat_2, lon_2 = p2
    Δ_lat = radians(lat_2 - lat_1)
    Δ_lon = radians(lon_2 - lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sin(Δ_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(Δ_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return r * c
