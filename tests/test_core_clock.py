import pytest
import time
from core.clock import Clock

def test_clock_now(monkeypatch):
    monkeypatch.setattr(time, "time", lambda: 123456)
    c = Clock()
    assert c.now() == 123456
