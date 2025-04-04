#!/usr/bin/env bash
set -e

API_PACKAGE_NAME="endurosat_api"

# Unfortunately, we have to keep to python-legacy to make it consistent with the jar output
CLIENT_NAME="python-legacy"

GENERATOR_OUTPUT=$(curl -X POST \
    "http://api-latest-master.openapi-generator.tech/api/gen/clients/$CLIENT_NAME" \
    -H "Accept: */*" \
    -H "Content-Type: application/json" \
    -d "{\"openAPIUrl\":
    \"https://api.ground-station.endurosat.com/v3/api-docs\",\"options\":
    {\"generateSourceCodeOnly\":true,\"packageName\":\"$API_PACKAGE_NAME\"}}")

echo $GENERATOR_OUTPUT
# This ugly substitution is necessary because no `jq` on the docker image
ZIP_LOCATION=$(echo $GENERATOR_OUTPUT | sed -e 's/.*\"link\":\"\(.*\)\"\}/\1/')
echo $ZIP_LOCATION name $ZIP_FILE_NAME

ZIP_FILE_NAME="output.zip"

wget $ZIP_LOCATION -O $ZIP_FILE_NAME

GENERATOR_OUTPUT_FOLDER="online_generator_output"
unzip $ZIP_FILE_NAME -d $GENERATOR_OUTPUT_FOLDER

echo "Output has a $CLIENT_NAME-client folder inside, need to move it"
# Remove if it exists
if [ -d $API_PACKAGE_NAME ]; then
    rm -r -v $API_PACKAGE_NAME
fi
mv $GENERATOR_OUTPUT_FOLDER/$CLIENT_NAME-client/$API_PACKAGE_NAME \
    $API_PACKAGE_NAME -v

rm -r -v online_generator_output $ZIP_FILE_NAME

echo "Cleaned up and generate files in $API_PACKAGE_NAME"
