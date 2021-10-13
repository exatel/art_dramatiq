#!/bin/bash

export UNIT_TESTS=1
export PYTHONPATH=$PYTHONPATH:/code
pytest
