import tasks


def test_adding(stub_broker, stub_worker):
    msg = tasks.sleep_and_add.send(20, 22)
    stub_broker.join(tasks.sleep_and_add.queue_name)
    stub_worker.join()
    assert msg.get_result(block=True) == 42
