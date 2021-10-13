import pytest
from dramatiq import Worker

from tasks import broker


@pytest.fixture()
def stub_broker():
    broker.flush_all()
    return broker


@pytest.fixture()
def stub_worker():
    worker = Worker(broker, worker_timeout=100)
    worker.start()
    yield worker
    worker.stop()
