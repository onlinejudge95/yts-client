#! /bin/bash

COVERAGE_DIR="./coverage"
if [ ! -d "$COVERAGE_DIR" ]; then
    mkdir $COVERAGE_DIR
fi

COVERAGE_UNIT_DIR="$COVERAGE_DIR/unit"
if [ ! -d "$COVERAGE_UNIT_DIR" ]; then
    mkdir $COVERAGE_UNIT_DIR
fi
pytest test/unit --cov-report xml:coverage/xml/unit
