import time
import pytest
from stream.message import Message
from stream.message_source import MessageSource
from stream.minibatch import MiniBatch
from stream.minibatch_builder import MiniBatchBuilder

def test_message_simple():
    msg = Message(value="hello")
    assert msg.value == "hello"

def test_minibatch_add_and_len():
    batch = MiniBatch()
    batch.add(Message("one"))
    batch.add(Message("two"))
    assert len(batch) == 2
    assert [m.value for m in batch.messages] == ["one", "two"]

def test_message_source_emits_many(monkeypatch):
    # monkeypatch Poisson generator for deterministic emission
    calls = []
    def fake_emit(callback):
        for i in range(5):
            callback(Message(f"msg_{i}"))
    monkeypatch.setattr(MessageSource, "start", lambda self: fake_emit(self._notify))
    source = MessageSource(rate_per_minute=10)
    collected = []
    source.subscribe(collected.append)
    source.start()
    assert len(collected) == 5

def test_batch_builder_batches(monkeypatch):
    pool_submitted = []
    class FakePool:
        def submit(self, task):
            pool_submitted.append(task)
    builder = MiniBatchBuilder(worker_pool=FakePool(), window_seconds=0)
    # add messages
    for i in range(7):
        builder.add_message(Message(f"v{i}"))
    # force flush
    builder._flush()
    assert len(pool_submitted) == 1
    assert isinstance(pool_submitted[0].messages, list)
