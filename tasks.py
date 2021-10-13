import time
import os

import dramatiq

# setup redis broker
from dramatiq.brokers.redis import RedisBroker
from dramatiq.brokers.stub import StubBroker
from dramatiq.results.backends import RedisBackend, StubBackend
from dramatiq.results import Results

if os.getenv("UNIT_TESTS") == "1":
    broker = StubBroker()
    stub_backend = StubBackend()
    broker.add_middleware(Results(backend=stub_backend))
    dramatiq.set_broker(broker)
else:
    broker = RedisBroker(host="redis")
    results_backend = RedisBackend(host="redis")
    broker.add_middleware(Results(backend=results_backend))
    dramatiq.set_broker(broker)


@dramatiq.actor
def hello_queue():
    print("Hello world!")


class ClassBasedActor(dramatiq.GenericActor):
    def perform(self):
        print("Hello from class based actor!")


@dramatiq.actor(max_retries=2)
def task_to_retry():
    print("Running task")
    raise RuntimeError("Error occurred")


@dramatiq.actor(max_age=1000, time_limit=5000)
def time_limited_task():
    print("I must hurry")
    try:
        time.sleep(6.0)
    except dramatiq.middleware.time_limit.TimeLimitExceeded as e:
        print("Ugh, I didn't get it done in time")


@dramatiq.actor(priority=0)
def high_priority_task(index):
    print(f"I'm a very important {index}")
    time.sleep(1.0)


@dramatiq.actor(priority=100)
def low_priority_task(index):
    print(f"I'm not so important {index}")
    time.sleep(2.0)


@dramatiq.actor(store_results=True)
def sleep_and_add(x, y):
    print("Got adding task, calculating")
    time.sleep(2.0)
    return x + y
