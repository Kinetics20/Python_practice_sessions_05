from math import isclose

import pytest

from main.fn_haversine import haversine, KM, MI, NM


def test_haversine_same_point():
    assert haversine((52.2296756, 21.0122287), (52.2296756, 21.0122287)) == 0


def test_haversine_known_distance():
    p1 = (52.2296756, 21.0122287)
    p2 = (50.0646501, 19.9449799)
    expected_km = 252
    result = haversine(p1, p2, KM)
    assert isclose(result, expected_km, rel_tol=0.01)


def test_haversine_units():
    p1 = (34.052235, -118.243683)
    p2 = (40.712776, -74.005974)

    result_km = haversine(p1, p2, KM)
    result_mi = haversine(p1, p2, MI)
    result_nm = haversine(p1, p2, NM)

    assert isclose(result_km, 3940, rel_tol=0.01)
    assert isclose(result_mi, 2449, rel_tol=0.01)
    assert isclose(result_nm, 2127, rel_tol=0.01)


def test_haversine_equator():
    p1 = (0, 0)
    p2 = (0, 90)
    expected_km = 10007
    assert isclose(haversine(p1, p2, KM), expected_km, rel_tol=0.01)


def test_haversine_poles():
    p1 = (90, 0)
    p2 = (-90, 0)
    expected_km = 20015
    assert isclose(haversine(p1, p2, KM), expected_km, rel_tol=0.01)


def test_haversine_negative_coordinates():
    p1 = (-33.9249, 18.4241)
    p2 = (-34.6037, -58.3816)
    expected_km = 6850
    assert isclose(haversine(p1, p2, KM), expected_km, rel_tol=0.01)


def test_haversine_custom_radius():
    MARS_RADIUS_KM = 3389.5
    p1 = (0, 0)
    p2 = (0, 90)
    expected_km = MARS_RADIUS_KM * 3.14159 / 2
    assert isclose(haversine(p1, p2, MARS_RADIUS_KM), expected_km, rel_tol=0.01)
