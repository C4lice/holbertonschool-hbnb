#!/bin/bash

sleep infinity & PID=$!
trap 'kill $PID' INT TERM

PYTHON=$(which python3)
BACK=$(realpath ./part3/run.py)
FRONT=$(realpath ./part4)

/bin/sh -ec ''"'$PYTHON'"' '"'$BACK'"' &'
/bin/sh -ec ''"'$PYTHON'"' -m http.server -d '"'$FRONT'"' &'
/bin/sh -ec 'open http://localhost:8000'

wait

fuser -n tcp 5000 | grep -o -E '[0-9]+' | xargs kill
fuser -n tcp 8000 | grep -o -E '[0-9]+' | xargs kill