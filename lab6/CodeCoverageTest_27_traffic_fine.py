
import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


# Tests for speeding_fine()

def test_no_speeding():
    assert speeding_fine(50, 60, "city") == 0


def test_school_zone_fine():
    assert speeding_fine(70, 50, "school") == 2000


def test_highway_fine():
    assert speeding_fine(70, 50, "highway") == 1000


def test_city_fine():
    assert speeding_fine(70, 50, "city") == 500



def test_excess_speed_above_40():
    assert speeding_fine(100, 50, "city") == 1500


def test_excess_speed_above_20():
    assert speeding_fine(80, 50, "city") == 1000


def test_excess_speed_20_or_less():
    assert speeding_fine(70, 50, "city") == 500


# Tests for license_action()

def test_clean_record():
    assert license_action(2, False, False) == "none"


def test_notice():
    assert license_action(4, False, False) == "notice"


def test_warning():
    assert license_action(8, False, False) == "warning"


def test_repeat_offender_suspended():
    assert license_action(8, False, True) == "suspend"


def test_commercial_license_revoked():
    assert license_action(12, True, False) == "revoke"


def test_noncommercial_license_suspended():
    assert license_action(12, False, False) == "suspend"


# Tests for total_penalty()

def test_total_penalty_normal():
    assert total_penalty([100, 200, 300]) == 600


def test_total_penalty_empty_list():
    assert total_penalty([]) == 0


def test_negative_fine_raises_error():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -50, 200])


def test_total_penalty_capped_at_10000():
    assert total_penalty([6000, 5000]) == 10000
