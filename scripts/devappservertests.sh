#!/bin/bash

## Run this script from the root of the TES project (ie: below src)

# start the dev appserver
echo
echo "*******************"
echo Start the appserver
echo "*******************"
echo
/opt/google/google_appengine/dev_appserver.py --port 8081 --clear_datastore --skip_sdk_update_check "./src" &
sleep 5

# call the dev appserver
echo
echo "*******************"
echo Run the tests
echo "*******************"
echo
response=$(curl --write-out %{http_code} --silent --output /dev/null http://localhost:8081/tests -d "")
echo Response is $response

# stop the dev appserver (could do something smarter here to parse the pid returned from starting
# the server, but hey)
echo
echo "*******************"
echo Stop the appserver
echo "*******************"
echo
killall python

if [ $response -eq 0 ]; then
        exit 1
    fi
if [ $response -ne 200 ]; then
        exit $response
    fi
