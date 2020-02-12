import pytest
import molpy


@pytest.mark.parametrize("point1, point2, bench", [([0, 1], [0, 0], 1), ([1, 1], [1, 1], 0), ([1, 0, 0], [0, 0, 0], 1)])

def test_distance(point1, point2, bench):

    assert molpy.util.distance(point1, point2) == bench
    ## assert molpy.util.distance([0, 1], [0, 0]) == 1
    ## assert molpy.util.distance([1, 1], [1, 1]) == 0
    ## assert molpy.util.distance([1, 0, 0], [0, 0, 0]) == 1