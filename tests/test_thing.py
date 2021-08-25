import pytest

import pyiot
from pyiot.thing import Thing, WindowSensor


def test_Thing():
    th = Thing()
    assert f"{th}" == "Thing(name=thing, xtype=thing)"


def test_Thing_named():
    th = Thing(name="thething")
    assert f"{th}" == "Thing(name=thething, xtype=thing)"


def test_Thing_invalid_arg():
    with pytest.raises(TypeError):
        th = Thing(eric="thething")


def test_wsensor():
    ws = WindowSensor()
    assert f"{ws}" == "WindowSensor(name=wsensor, xtype=sensor)"


def test_wsensor_with_type():
    ws = WindowSensor(xtype="thingy")
    assert f"{ws}" == "WindowSensor(name=wsensor, xtype=thingy)"


def test_ws_status():
    ws = WindowSensor(xtype="thingy")
    ws.wclose()
    assert ws.status is True


def test_ws_open():
    ws = WindowSensor(xtype="thingy")
    ws.wopen()
    assert ws.status is False


def test_ws_not_open():
    ws = WindowSensor(xtype="thingy")
    ws.wclose()
    assert ws.status is not False
