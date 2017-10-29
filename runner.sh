#!/bin/bash
set -e
if [ ! -d "test" ]; then
    mkdir test
fi

python prepare_datasets_DRIVE.py
python run_training.py
python run_testing.py
