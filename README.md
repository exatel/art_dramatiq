### What is this
This repository contains source code used in the dramatiq article the Exatel blog.
It covers basing usage and testing tasks defined and run using dramatiq library (https://dramatiq.io/).

### Running 
Examples (tasks_sender, worker, redis) can be run simply using docker-compose:

`docker-compose up`

Edit main.py to send different tasks to the worker.


### Unit testing
Unit tests can be run with run_unit_tests.sh within tasks_sender container:

`docker-compose run --rm task_sender ./run_unit_tests.sh`

### LICENSE
See [LICENSE](./LICENSE).

### Authors
 - Szymon Nogieć
