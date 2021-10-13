import tasks
import dramatiq.results.errors


def basic_example():
    for i in range(3):
        print(f"Sending task nr {i}")
        tasks.hello_queue.send()


def class_based_actor():
    tasks.ClassBasedActor.send()


def retries():
    tasks.task_to_retry.send()


def time_limited_task():
    tasks.time_limited_task.send()


def send_with_delay():
    print("Sending task with delay")
    tasks.time_limited_task.send_with_options(delay=500)


def priorities():
    print("Sending 20 low prio tasks")
    for i in range(20):
        tasks.low_priority_task.send(i)
    print("Sending 5 high prio tasks")
    for i in range(5):
        tasks.high_priority_task.send(i)


def results():
    msg = tasks.sleep_and_add.send(2, 2)
    try:
        result = msg.get_result(block=False)
    except dramatiq.results.errors.ResultMissing:
        print("Result is not ready yet...")
        result = msg.get_result(block=True)
        print(f"Result is {result}")


def main():
    # basic_example()
    # class_based_actor()
    # retries()
    # time_limited_task()
    # send_with_delay()
    # priorities()
    results()


if __name__ == '__main__':
    main()
