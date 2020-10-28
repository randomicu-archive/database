#!/bin/bash

sleep 3

/opt/pysetup/.venv/bin/yoyo apply -vvv --batch --database ${FAKEDATA_DATABASE_URL}
