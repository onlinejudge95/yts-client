#! /bin/bash

COVERAGE_DIR="./coverage"
if [ ! -d "$COVERAGE_DIR" ]; then
    mkdir $COVERAGE_DIR
fi

COVERAGE_E2E_DIR="$COVERAGE_DIR/e2e"
if [ ! -d "$COVERAGE_E2E_DIR" ]; then
    mkdir $COVERAGE_E2E_DIR
fi
pytest test/e2e --cov-report xml:coverage/xml/e2e
