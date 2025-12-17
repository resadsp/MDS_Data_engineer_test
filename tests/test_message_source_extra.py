from stream.message_source import MessageSource
from stream.message import Message

def test_message_source_reads():
    msgs = [Message("a"), Message("b")]
    source = MessageSource(msgs)
    read_msgs = list(source.read())
    assert read_msgs == msgs


def test_message_source_iterable():
    msgs = [Message("a"), Message("b")]
    source = MessageSource(msgs)
    # ako je iterator implementiran
    read_msgs = list(source)
    assert read_msgs == msgs
