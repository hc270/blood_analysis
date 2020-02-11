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


