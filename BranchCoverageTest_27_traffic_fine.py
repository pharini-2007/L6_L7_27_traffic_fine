
import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


def test_speed_at_limit():
    assert speeding_fine(50, 50, "city") == 0


def test_speed_above_limit_school_zone():
    assert speeding_fine(60, 50, "school") == 2000


def test_speed_above_limit_highway():
    assert speeding_fine(60, 50, "highway") == 1000


def test_speed_above_limit_other_zone():
    assert speeding_fine(60, 50, "city") == 500


def test_excess_above_40():
    assert speeding_fine(100, 50, "city") == 1500


def test_excess_exactly_40():
    assert speeding_fine(90, 50, "city") == 1000


def test_excess_above_20():
    assert speeding_fine(80, 50, "city") == 1000


def test_excess_exactly_20():
    assert speeding_fine(70, 50, "city") == 500


def test_points_at_least_12_commercial():
    assert license_action(12, True, False) == "revoke"


def test_points_at_least_12_noncommercial():
    assert license_action(12, False, False) == "suspend"


def test_points_8_repeat_offender():
    assert license_action(8, False, True) == "suspend"


def test_points_8_not_repeat_offender():
    assert license_action(8, False, False) == "warning"


def test_points_4():
    assert license_action(4, False, False) == "notice"


def test_points_below_4():
    assert license_action(3, False, False) == "none"


def test_empty_fines():
    assert total_penalty([]) == 0


def test_single_fine():
    assert total_penalty([500]) == 500


def test_multiple_fines():
    assert total_penalty([100, 200, 300]) == 600


def test_negative_fine():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -1, 200])


def test_total_above_cap():
    assert total_penalty([6000, 5000]) == 10000


def test_total_equal_to_cap():
    assert total_penalty([4000, 6000]) == 10000


def test_total_below_cap():
    assert total_penalty([4000, 5000]) == 9000
