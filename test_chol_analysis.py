import pytest


def test_HDL_analysis():
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer -- expected
    """
    from chol_analysis import HDL_analysis
    input = 100
    answer = HDL_analysis(input)
    expected = 'Normal'
    assert answer == expected


def test_LDL_analysis():
    """Parametrize Tests HDL_analysis method
    Args:
        HDL_level
    Returns:
        Passed if answer -- expected
    """
    from chol_analysis import LDL_analysis
    input = 100
    answer = LDL_analysis(input)
    expected = 'Normal'
    assert answer == expected


@pytest.mark.parametrize("input, output, expected", [
    (100, 'Normal', True),
    (50, 'Borderline low', True),
    (20, 'Low', True),
])
def test_HDL_analysis2(input, output, expected):
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(input) == output
    assert answer == expected
