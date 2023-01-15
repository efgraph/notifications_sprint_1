#!/bin/bash

echo "Waiting for event api is OK"
python src/api_check.py

pytest -W ignore::DeprecationWarning