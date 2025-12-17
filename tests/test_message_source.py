import pytest
from src.stream.message_source import MessageSource
from src.stream.message import Message

# Ako MessageSource implementira __iter__ (što je verovatno slučaj)
def test_message_source_yields_messages():
    msgs = [Message("x"), Message("y")]
    src = MessageSource(msgs)
    out = list(src)  # Ako je MessageSource iterator
    assert out == msgs
