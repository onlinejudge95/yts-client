#! /bin/bash

COVERAGE_DIR="./coverage"
if [ ! -d "$COVERAGE_DIR" ]; then
    mkdir $COVERAGE_DIR
fi

COVERAGE_INTEG_DIR="$COVERAGE_DIR/integ"
if [ ! -d "$COVERAGE_INTEG_DIR" ]; then
    mkdir $COVERAGE_INTEG_DIR
fi
pytest test/integration --cov-report xml:coverage/xml/integration
