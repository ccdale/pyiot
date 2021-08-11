import pytest

from pyiot import __version__
from pyiot import errorNotify, errorRaise, errorExit


def test_version():
    assert __version__ == "0.1.0"


def test_errorNotify(capsys):
    with pytest.raises(Exception) as excinfo:
        raise Exception("a test exception")
    errorNotify(excinfo.tb, excinfo.value)
    captured = capsys.readouterr()
    xout = captured.out
    assert (
        xout
        == f"Exception Exception at line 13 in function test_errorNotify: a test exception\n"
    )


def test_errorRaise(capsys):
    with pytest.raises(Exception) as excinfo:
        raise Exception("a test exception")
    with pytest.raises(Exception) as excinfo2:
        errorRaise(excinfo.tb, excinfo.value)
    captured = capsys.readouterr()
    xout = captured.out
    assert (
        xout
        == f"Exception Exception at line 25 in function test_errorRaise: a test exception\n"
    )
    assert excinfo2.tb.tb_lineno == 27


def test_errorExit(capsys):
    with pytest.raises(Exception) as excinfo:
        raise Exception("a test exception")
    with pytest.raises(SystemExit) as excinfo2:
        errorExit(excinfo.tb, excinfo.value)
    captured = capsys.readouterr()
    xout = captured.out
    assert (
        xout
        == f"Exception Exception at line 39 in function test_errorExit: a test exception\n"
    )
    assert excinfo2.tb.tb_lineno == 41
    assert excinfo2.value.code == 1
