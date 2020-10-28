#!/bin/bash

sleep 2

/opt/pysetup/.venv/bin/yoyo apply -vvv --batch --database ${FAKEDATA_DATABASE_URL}
